from undervisningsadminstrasjon import Undervisningsadminstrasjon

admin = Undervisningsadminstrasjon()
admin.lesFilAktivitetEmner("fil1.txt")
admin.lesFilStudenter("fil2.txt")
admin.skrivGruppeMedLavtOppmoete(8)
admin.skrivUtAktiviteter()