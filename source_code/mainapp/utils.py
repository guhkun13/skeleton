from django.db.models import Q
from django.db.models import Sum
from .models import *

def get_data_dashboard():

    biller_all              = Mapping.objects.using('switching').all()
    total_biller_all        = biller_all.count()
    total_biller_p2h        = biller_all.filter(tipe_biller='P2H').count()
    total_biller_h2h        = biller_all.filter(tipe_biller='H2H').count()


    # Trx
    trx_all                 = Payment.objects.using('billing').all()
    trx_all_success         = trx_all.filter(rc='00',status_bayar='1')
    total_trx_all           = trx_all.count()
    total_trx_all_success   = trx_all_success.count()
    total_trx_all_canceled  = total_trx_all - total_trx_all_success
    total_trx_today         = 10

    # Nominal Trx
    total_nominal_trx_all           = trx_all.aggregate(Sum('nominal_bayar'))['nominal_bayar__sum'] or None
    total_nominal_trx_all_success   = trx_all_success.aggregate(Sum('nominal_bayar'))['nominal_bayar__sum'] or None
    total_nominal_trx_all_canceled  = total_nominal_trx_all - total_nominal_trx_all_success
    total_nominal_trx_today         = 10

    # Percentage
    percentage_trx_all_success      = percentage(total_trx_all_success, total_trx_all)

    result = {
        'total_biller_all'                  : total_biller_all,
        'total_biller_p2h'                  : total_biller_p2h,
        'total_biller_h2h'                  : total_biller_h2h,

        'total_trx_all'                     : total_trx_all,
        'total_trx_all_success'             : total_trx_all_success,
        'total_trx_all_canceled'            : total_trx_all_canceled,
        'total_trx_today'                   : total_trx_today,

        'total_nominal_trx_all'             : total_nominal_trx_all,
        'total_nominal_trx_all_success'     : total_nominal_trx_all_success,
        'total_nominal_trx_all_canceled'     : total_nominal_trx_all_canceled,
        'total_nominal_trx_today'           : total_nominal_trx_today,

        'percentage_trx_all_success'        : percentage_trx_all_success,
    }

    return result

def percentage(part, whole):
    result = 100 * float(part)/float(whole)
    result = round(result, 2)

    return result
