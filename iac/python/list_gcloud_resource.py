import os

print("GCLOUD CLUSTER LIST IN ALL LOCATIONS \n")
os.system("gcloud container clusters list")
print("\n")
print("ALL GCP PROJECTS LIST \n")
os.system("gcloud projects list --page-size=30")