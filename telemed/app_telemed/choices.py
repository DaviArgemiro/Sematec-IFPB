from .models import Medico

medic_choices = ()
tmp = []

medicos = Medico.objects.all()

for medico in medicos:
    tmp.append((medico.id, f"{medico.first_name} {medico.last_name} - {medico.areaAtuacao}"))

medic_choices = tuple(tmp)