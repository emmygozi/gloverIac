provider "google" {
  credentials = file("CREDENTIALS_FILE.json")
  project     = var.project.id
  region      = "us-central1"
}