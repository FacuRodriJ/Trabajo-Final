from django.db import models


class Establecimiento(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=150)
    # dirección
    # horarios atendiendo
    # si exige seña
    # colaboradores asignados

    # Relación uno a muchos - Propietario Establecimiento
    propietario = models.ForeignKey('app_cuentas.Propietario', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['nombre']


class Cancha(models.Model):
    SUPERFICIES = (
        (1, 'Césped artificial'),
        (2, 'Césped natural'),
        (3, 'Piso'),
        (4, 'Arena')
    )
    CAPACIDAD = (
        (1, '5'),
        (2, '6'),
        (3, '7'),
        (4, '8'),
        (5, '9'),
        (6, '11'),
    )
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    superficie = models.CharField(verbose_name="Superficie", max_length=60, choices=SUPERFICIES)
    capacidad = models.CharField(verbose_name="Capacidad", max_length=2, choices=CAPACIDAD)

    # Relación uno a muchos - Establecimiento Cancha
    establecimiento = models.ForeignKey(Establecimiento, on_delete=models.CASCADE)


class Reserva(models.Model):
    jugador = models.ForeignKey('app_cuentas.Jugador', on_delete=models.PROTECT)
    cancha = models.ForeignKey(Cancha, on_delete=models.PROTECT)

