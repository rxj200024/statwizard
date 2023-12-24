from rest_framework import serializers

class AveragesSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    first = serializers.CharField()
    last = serializers.CharField()
    pts = serializers.FloatField()
    reb = serializers.FloatField()
    ast = serializers.FloatField()
    stl = serializers.FloatField()
    blk = serializers.FloatField()
    tov = serializers.FloatField()