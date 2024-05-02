from flask import Flask, request
from kubernetes import client, config

app = Flask(__name__)

# Load Kubernetes configuration
config.load_incluster_config()
# Create a Kubernetes API client
v1 = client.BatchV1Api()


@app.route("/runjob", methods=["POST"])
def run_job():
    # Job name (optional: get from request if needed)
    job_name = "generate"

    # Define the job spec
    job = client.V1Job(
        api_version="batch/v1",
        kind="Job",
        metadata=client.V1ObjectMeta(name=job_name),
        spec=client.V1JobSpec(
            template=client.V1PodTemplateSpec(
                spec=client.V1PodSpec(
                    containers=[client.V1Container(
                        name="jgeneratedata",
                        image="alakh1111/jgeneratedata_kube",
                        #image="busybox:latest",  # Use a simple image like busybox
                        #command=["sh", "-c", "echo 'Hello, talend!' && sleep 30"],
                    )],
                    restart_policy="Never",
                )
            )
        )
    )

    # Create the job
    try:
        v1.create_namespaced_job(namespace="default", body=job)
        return f"Job '{job_name}' created successfully", 201
    except Exception as e:
        return f"Error creating job: {e}", 500


if __name__ == "__main__":
    app.run(debug=True)