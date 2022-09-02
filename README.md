# gloverIac







docker.io/emmygozi/glover




<!-- ABOUT THE PROJECT -->
## About The Project
The project is hosted in a kubernetes cluster on: http://34.122.59.193/

This repository contains the cloned repository, terraform code, python script and kubernetes helm chart used to deploy the application.

Here's a breakdown:
* laravel folder is located at `abc-article-api` it contains the `Dockerfile` to containerize the app

* Terrform folder is located at `iac` > `terraform` 

* Python folder is located at `iac` > `python` 
* Kubernetes helm chart is located at `glover-kubernetes`


## Steps to use
clone project
```
git clone https://github.com/emmygozi/gloverIac.git
cd gloverIac
```
#### Terraform
Make sure you have terraform installed https://www.terraform.io/downloads
Make sure you download your GCP service account json credentials https://developers.google.com/workspace/guides/create-credentials
```
cd iac/terraform
```
Replace the `CREDENTIAL_FILE.json` with your downloaded json in `provider.tf` then run
```
terraform init
```
Enter your GCP project ID when prompted. You can locate it on your GCP console.

The abbove command creates a folder named `.terraform`

Comment out username and password on line 21 and 22 in this file `.terraform/modules/cluster/vpc-native/main.tf`

Then run the following to spin up a kubernetes cluster
```
terrform plan
terraform apply
gcloud container clusters get-credentials CLUSTER_NAME
```

NB: Best practice is to connect terraform backend state with cloud bucket or terraform cloud to maintain secured state file https://www.terraform.io/cloud-docs. This is an area this project can be improved upon.

### Python
Make sure you have python3 installed https://www.python.org/

Run the following to list out your cluster created with terraform above and other resources
```
cd iac/python
python3 list_gcloud_resource.py
```

### Laravel Docker Image
The current hosted image is connected to an online mysql DB.

Check `README.md` in the folder location for more information ` abc-article-api`

```
cd abc-article-api
docker build -t devops/article-api:latest .
docker run -p 8080:8080 devops/article-api:latest
```

### Kubernetes
Install Kubectl and Helm on your device and run
```
helm install glover-chart glover-kubernetes/ --values glover-kubernetes/values.yaml
```
This would install the application in your newly created kubernetes cluster. It would also pull an already published version of the laravel image from `docker hub`

Finally, destroy all GKE resources created to save cost
```
terraform destroy
```

## Built With


* [![Laravel][Laravel.com]][Laravel-url]
* [![Terraform][Terraform.io]][Terraform-url]
* [![Kubernetes][Kubernetes.io]][Kubernetes-url]
* [![Python][Python.org]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[Terraform.io]: https://img.shields.io/badge/terraform-%235835CC.svg?style=for-the-badge&logo=terraform&logoColor=white
[Terraform-url]: https://terraform.io
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Kubernetes.io]: https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white
[Kubernetes-url]: https://kubernetes.io
[Kubernetes.io]: https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white
[Python-url]: https://python.org
[Python.org]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54