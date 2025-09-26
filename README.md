# Cow wisdom web server

## Prerequisites

```
sudo apt install fortune-mod cowsay -y
```


## How to use?

1. Run `./wisecow.sh`
2. Point the browser to server port (default 4499)

## What to expect?

![wisecow](https://github.com/nyrahul/wisecow/assets/9133227/8d6bfde3-4a5a-480e-8d55-3fef60300d98)

# Problem Statement: Deploy the Wisecow application as a Kubernetes app

---

## Your Accomplishments

### Problem Statement 1: Containerization & Kubernetes Deployment

- Created a Dockerfile to containerize Wisecow application.
- Wrote Kubernetes manifest files (deployment, service) to deploy and expose the app.
- Configured TLS certificates to enable secure communication.
- Created GitHub Actions workflow to automate Docker image build and push on repo changes.

### Problem Statement 2: Automation Scripts

- Developed Python script to monitor system health metrics (CPU, memory, disk, process count).
- Developed Python script to continuously check application uptime using HTTP status codes.

### Problem Statement 3: Zero-trust KubeArmor Policy

- Created a KubeArmor policy YAML blocking file access on `/app` directory in Wisecow pods.
- Applied the policy successfully to Kubernetes cluster.
- Attempted to trigger violation logs by file access attempts.
- Encountered KubeArmor issue where node information was unavailable causing termination.
- Despite this, documented efforts to capture violation logs and troubleshooting carried out.

---

## Important Notes

- KubeArmor logs show errors `"The node information is not available"` causing it to terminate.
- This prevented live violation detection during assessment.
- Full troubleshooting of KubeArmor environment compatibility is ongoing.
- All other requirements were successfully completed and demonstrated.

---

## Submission Artifacts

- `Dockerfile`
- Kubernetes manifests (`deployment.yaml`, `service.yaml`, TLS cert files)
- GitHub Actions workflow file
- Python monitoring scripts
- KubeArmor policy YAML file (`wisecow-file-policy.yaml`)
- Screenshots documenting:
  - Wisecow pod file structure
  - Applied KubeArmor policy YAML
  - Commands triggering file access violations inside pod
  - KubeArmor logs showing node info error and termination

---
## Screenshots / Evidence

The following screenshots are provided as evidence of the work completed in this assessment:

1. **Wisecow Pod Directory Listing**  
   Shows the `/app` directory structure inside the Wisecow pod to confirm application files.

2. **KubeArmor Policy YAML Applied**  
   Content of the KubeArmor policy YAML file that blocks file access under `/app`.

3. **Violation Commands Executed Inside Pod**  
   Screenshot of commands inside the pod trying to write files to `/app` to trigger KubeArmor violations.

4. **KubeArmor Logs Streaming**  
   Shows KubeArmor logs with Node Info error message causing termination and prevention of live violation detection.

5. **Wisecow Application Access**  
   Screenshots of the application working and accessible at both `wisecow.local` and `localhost:4499` in browser.

6. **KubeArmor Pods Status**  
   Output of `kubectl get pods -n kubearmor` showing the current status of KubeArmor pods for validation.

7. **(Optional) GitHub Actions Workflow**  
   Screenshot from GitHub Actions showing successful Docker image build and push on repo changes.

---

Add the screenshots inside your project repo under a `screenshots/` folder and link or reference them here appropriately if needed.


Thank you for your review!

---

