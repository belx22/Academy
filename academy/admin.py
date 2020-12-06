from django.contrib import admin

# Register your models here.

from .models import Cours, Chapitre , Quiz, Etudiant, Videos, Enseignant, Commentaire, Onligne
# Register your models here.
admin.site.site_header = "Administration du site"
admin.site.register(Cours)
admin.site.register(Chapitre)
admin.site.register(Etudiant)
admin.site.register(Videos)
admin.site.register(Enseignant)
admin.site.register(Quiz)
admin.site.register(Commentaire)
admin.site.register(Onligne)

