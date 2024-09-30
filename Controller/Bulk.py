class Bulk:
    def __init__(self):

        self.Bulk_class = None
        self.Bulk_skel = None
        self.Bulk_species = None

        # Méthodes de setter pour chaque attribut
    def set_bulk_class(self, class_value):
        self.Bulk_class = class_value

    def set_bulk_skel(self, skel_value):
        self.Bulk_skel = skel_value

    def set_bulk_species(self, species_value):
        self.Bulk_species = species_value

    # Méthodes de getter pour chaque attribut
    def get_bulk_class(self):
        return self.Bulk_class

    def get_bulk_skel(self):
        return self.Bulk_skel

    def get_bulk_species(self):
        return self.Bulk_species