# Best Practices & Deployment Strategy for GCP using Terraform, Google ADK Agents, Cloud Run, and GitLab

## Best Practices for Terraform on GCP
- **Plan before applying:** Always use `terraform plan` first to preview changes before `terraform apply`.
- **Automate via CI/CD:** Implement Terraform runs in an automated pipeline to ensure consistent and repeatable provisioning.
- **Use service accounts:** Employ dedicated service accounts with least privilege permissions for Terraform automation.
- **Manage state securely:** Use remote backends like **Google Cloud Storage** with locking to store Terraform state safely.
- **Limit custom scripts:** Avoid unmanaged scripts outside Terraform to prevent state drift and unmanaged resources.
- **Modularize code:** Organize infrastructure code with reusable Terraform modules for components like networks, IAM roles, and Cloud Run services.

---

## Deploying Google ADK Agents on Cloud Run
- Use the `adk deploy cloud_run` command to deploy your agents seamlessly.
- This command:
  - Packages your agent into a Docker container.
  - Pushes it to **Google Artifact Registry**.
  - Creates and deploys the **Cloud Run** service automatically.
- You can deploy multiple agents in one Cloud Run instance by structuring your project with separate folders for each agent.
- Manage environment variables, region, service name, and optionally enable the interactive UI for debugging.
- Alternatively, use `gcloud run deploy` with the necessary build and environment parameters.
- Monitor agent performance with **Cloud Trace** and manage traffic for safe rollouts and testing.

---

## Integrating GitLab for CI/CD
- Connect GitLab to your GCP project using **Workload Identity Federation** and IAM to secure permissions without service account keys.
- Store container images in **Google Artifact Registry** connected to GitLab.
- Use **GitLab Runner** (on GCP or GitLab’s shared runners) to execute Terraform and deployment jobs.
- Structure your GitLab pipeline:
  1. **Stage 1:** Plan and validate Terraform code.
  2. **Stage 2:** Apply Terraform to provision infrastructure.
  3. **Stage 3:** Build and push container images.
  4. **Stage 4:** Deploy to Cloud Run using Terraform or `gcloud` commands.
- Use GitLab CI templates and cache state to optimize runs.
- Implement a manual approval step before production Terraform apply for safety.
- Automate cleanup with `terraform destroy` as needed.
- Monitor logs and pipeline status for operational insight.

---

## High-Level Deployment Workflow
1. **Write Terraform code**: Define all infrastructure—networks, IAM roles, Cloud Run, Artifact Registry, service accounts.
2. **Store code in GitLab repo**: Version control your Terraform configs and agent app code.
3. **Set up GitLab CI pipeline:**
   - Terraform init, plan, and apply with cleanup stage.
   - Docker image build and push to Artifact Registry.
   - Deploy Cloud Run agent services with `adk deploy` or Terraform resources.
4. **Use environment-specific workspaces or variables** for multi-environment deployment.
5. **Enable logging, monitoring, and tracing** on Cloud Run to observe agent health and performance.
6. **Implement gradual rollout strategies** using Cloud Run’s traffic splitting for safe updates.

---

**✅ Key Takeaway:**  
Following these combined practices will give you a **robust, scalable, and manageable** deployment process for your application on GCP using **Terraform**, **Cloud Run with Google ADK agents**, and **GitLab CI/CD pipelines**.
