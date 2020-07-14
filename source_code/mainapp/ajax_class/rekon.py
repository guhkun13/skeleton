from django.db.models import Q
from mainapp.models import LogRekon

def isotime(param):
    result = (str(param)).replace('T', ' ')
    return result

class RekonClass:

    def get_all_data(self):
        return LogRekon.objects.using('billing').all()

    def filter_search(self, search):
        return LogRekon.objects.using('billing').filter(
                Q(ts__icontains=search)|
                Q(kode_biller__icontains=search)|
                Q(kode_bayar__icontains=search)|
                Q(tanggal_mulai__icontains=search)|
                Q(tanggal_akhir__icontains=search)|
                Q(nominal_rekon__icontains=search)|
                Q(rc__icontains=search)|
                Q(response_msg__icontains=search)
            )

    def generate_data(self, object_list):

        data = [
            {
                'ts': isotime(item.ts),
                'kode_biller': item.kode_biller,
                'kode_bayar': item.kode_bayar,
                'tanggal_mulai': item.tanggal_mulai,
                'tanggal_akhir': item.tanggal_akhir,
                'nominal_rekon': item.nominal_rekon,
                'rc': item.rc,
                'response_msg': item.response_msg,
                'ts_update': isotime(item.ts_update),
                'time_elapsed': self.calculate_time_elapsed(item.ts_update, item.ts),
            } for item in object_list
        ]

        return data


    def calculate_time_elapsed(self, ts_resp, ts):
        result = 'N/A'
        if (ts_resp and ts):
            result = ts_resp - ts
            result = result.total_seconds()

        return result
