from django.db.models import Q
from mainapp.models import Payment

def isotime(param):
    result = (str(param)).replace('T', ' ')
    return result

class TrxClass:

    def get_all_data(self, **kwargs):
      print('get_all_data Trx')
      data = Payment.objects.using('billing').all()
      year = kwargs.get('year')
    
      if year:
        print ('year = ', year)
        data = data.filter(ts__year=year)
      
      month = kwargs.get('month')
      if month and int(month) > 0:
        data = data.filter(ts__month=month)
      
      day = kwargs.get('day')
      if day and int(day) > 0:
        print ('filter by day ' + day)
        data = data.filter(ts__day=day)
      
      biller = kwargs.get('biller')
      if biller :
        print ('filter by biller ' + biller)
        data = data.filter(kode_biller=biller)
      
      nomor_bayar = kwargs.get('nomor_bayar')
      if nomor_bayar:
        print ('filter by nomor_bayar ' + nomor_bayar)
        data = data.filter(nomor_pembayaran=nomor_bayar)

      return data 
      
    def filter_search(self, search):
        return Payment.objects.using('billing').filter(
                Q(ts__icontains=search)|
                Q(no_jurnal__icontains=search)|
                Q(kode_biller__icontains=search)|
                Q(kode_channel__icontains=search)|
                Q(nama_channel__icontains=search)|
                Q(nama__icontains=search)|
                Q(nomor_pembayaran__icontains=search)|
                Q(nominal_bayar__icontains=search)|
                Q(status_bayar__icontains=search)|
                Q(rc__icontains=search)|
                Q(catatan__icontains=search)|
                Q(komentar__icontains=search)
            )

    def generate_data(self, object_list):
        data = [
            {
                'ts': isotime(item.ts),
                'kode_biller': item.kode_biller,
                'kode_channel': item.kode_channel,
                'nama_channel': item.nama_channel,
                'no_jurnal': item.no_jurnal,
                'nama': item.nama,
                'nomor_pembayaran': item.nomor_pembayaran,
                'nominal_bayar': item.nominal_bayar,
                'status_bayar': item.status_bayar,
                'rc': item.rc,
                'catatan': item.catatan,
                'komentar': item.komentar,
                'updated': isotime(item.updated),
                'time_elapsed': self.calculate_time_elapsed(item.updated, item.ts),
            } for item in object_list
        ]

        return data


    def calculate_time_elapsed(self, ts_resp, ts):
        result = 'N/A'
        if (ts_resp and ts):
            result = ts_resp - ts
            result = result.total_seconds()

        return result
