from django.db import models

class Station(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return str(self.name)

class Observation(models.Model):
    ObsID =  models.IntegerField()
    StartTime = models.DateTimeField()
    StopTime = models.DateTimeField()
    stations = models.ManyToManyField(Station)

    def __str__(self):
        return str(self.ObsID)


class StationObservation(models.Model):
    station = models.ForeignKey(Station, on_delete=models.SET_NULL, null=True)
    observation = models.ForeignKey(Observation, on_delete=models.CASCADE, null=False)
    ReceiverBitmap = models.CharField(max_length=100)
    HBABitmap = models.CharField(max_length=100)
    LBABitmap = models.CharField(max_length=100)


class Antenna(models.Model):
    name = models.CharField(max_length=10)
    station = models.ForeignKey(Station, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return str(self.station.name)+'_'+str(self.name)

# code can be 0, 10, 20, 30, 40, 50, 60 ,70
class AntennaState(models.Model):
    antenna = models.ForeignKey(Antenna, on_delete=models.CASCADE, null=False)
    state_code = models.IntegerField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return str(self.timestamp) + ":" + str(self.antenna) + ' ' + str(self.state_code)


# Create your models here.
class SensorData(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE, null=False)
    DataPointName = models.CharField(max_length=50)
    Value = models.FloatField()
    Unit = models.CharField(max_length=5)
    timestamp =  models.DateTimeField()

    def __str__(self):
        return str(self.timestamp) + ":" + str(self.station) + ' ' + str(self.DataPointName) + ' ' + str(self.Value) + ' ' + str(self.Unit)

