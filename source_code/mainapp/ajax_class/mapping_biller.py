from django.db.models import Q
from mainapp.models import Mapping

def isotime(param):
    result = (str(param)).replace('T', ' ')
    result = result.split('.')[0]
    return result

class MappingBillerClass:

    def get_all_data(self, year=None):
        return Mapping.objects.using('switching').all()

    def filter_search(self, search):
        return Mapping.objects.using('switching').filter(
                Q(updated_at__icontains=search)|
                Q(created_at__icontains=search)|
                Q(kode_biller__icontains=search)|
                Q(nama_biller__icontains=search)|
                Q(tipe_biller__icontains=search)|
                Q(tipe_bayar__icontains=search)|
                Q(url_inquiry__icontains=search)|
                Q(url_payment__icontains=search)|
                Q(url_reversal__icontains=search)|
                Q(catatan__icontains=search)|
                Q(creator__icontains=search)
            )

    def generate_data(self, object_list):
        data = [
            {
                'updated_at': isotime(item.updated_at),
                'created_at': isotime(item.created_at),
                'kode_biller': item.kode_biller,
                'nama_biller': item.nama_biller,
                'tipe_biller': item.tipe_biller,
                'tipe_bayar': item.tipe_bayar,
                'url_inquiry': item.url_inquiry,
                'url_payment': item.url_payment,
                'url_reversal': item.url_reversal,
                'catatan': item.catatan,
                'creator': item.creator,
            } for item in object_list
        ]

        return data


    def calculate_time_elapsed(self, ts_resp, ts):
        result = 'N/A'
        if (ts_resp and ts):
            result = ts_resp - ts
            result = result.total_seconds()

        return result
