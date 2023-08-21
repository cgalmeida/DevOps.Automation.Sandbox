# Create a resource group
resource "azurerm_resource_group" "resourcegroup_aulas" {
  name     = var.gruporecursos_aula
  location = var.localizacao
  tags = var.tags
}