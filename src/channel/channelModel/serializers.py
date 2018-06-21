from rest_framework import serializers
from channelModel.models import PpnCdmChannel

class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PpnCdmChannel
        fields = ('chan_id','chan_code','chan_name','chan_attach','chan_type','chan_hd_flag','chan_play_begin_time','chan_play_end_time','chan_desc','chan_begin_date','chan_end_date','chan_status','chan_play_site','chan_play_lang','chan_cover_zone','chan_field1','chan_field2','create_time','create_type','create_user')
