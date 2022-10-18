from .models import Medico

medic_choices = []

medicos = Medico.objects.all()

for medico in medicos:
    medic_choices.append((medico.id, f"{medico.first_name} {medico.last_name} - {medico.areaAtuacao}"))


