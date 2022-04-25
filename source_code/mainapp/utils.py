from itertools import cycle
from select import select
from statistics import mode
from django.db.models import Q
from django.db.models import Sum
from .models import *

_LOG_INQ = 'log_inquiry'
_LOG_PAY = 'log_payment'
_LOG_REV = 'log_reversal'
_TRX     = 'trx'

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

    # result['log_inquiry'] = get_summary_log(_LOG_INQ)
    # result['log_payment'] = get_summary_log(_LOG_PAY)
    # result['log_reversal'] = get_summary_log(_LOG_REV)
    # result['trx'] = get_summary_log(_TRX)
    # result['trx_amount'] = get_summary_trx_amount()

    return result

def percentage(part, whole):
    if whole < 1:
      whole = 1
    result = 100 * float(part)/float(whole)
    result = round(result, 2)

    return result

def get_summary_trx_amount():
  ret = []
  list_years = get_years_from_records(_TRX)
  qs_all = Payment.objects.using('billing').all()

  for item in list_years:
    print ('#', item['year'])
    temp_arr = {}
    
    qs = qs_all.filter(ts__year=item['year'])
    total_nominal_all = qs.aggregate(Sum('nominal_bayar'))['nominal_bayar__sum'] or None
    count_all = qs.count()
    print ('total_nominal_all %s ' % total_nominal_all)

    qs_ok = qs.filter(rc='00', status_bayar='1')
    total_nominal_success = qs_ok.aggregate(Sum('nominal_bayar'))['nominal_bayar__sum'] or None
    count_nominal_success = qs_ok.count()
    print ('total_nominal_success %s ' % total_nominal_success)

    total_nominal_success = 0 if total_nominal_success is None else total_nominal_success
    total_nominal_cancel = total_nominal_all - total_nominal_success
    count_nominal_cancel = count_all - count_nominal_success
    print ('total_nominal_cancel %s ' % total_nominal_cancel)

    temp_arr['year'] = item['year']
    temp_arr['count_all'] = count_all
    temp_arr['total_nominal'] = total_nominal_all

    temp_arr['count_nominal_success'] = count_nominal_success
    temp_arr['total_nominal_success'] = total_nominal_success

    temp_arr['count_nominal_cancel'] = count_nominal_cancel
    temp_arr['total_nominal_cancel'] = total_nominal_cancel

    ret.append(temp_arr)
  
  return ret
  

from django.db.models import Count
from django.db.models.functions import ExtractMonth, ExtractYear

def get_years_from_records(model_name):
  qs = None
  if model_name == _LOG_INQ:    
    qs = LogInquiry.objects.using('billing').values(year=ExtractYear('ts'))
  elif model_name == _LOG_PAY:    
    qs = LogPayment.objects.using('billing').values(year=ExtractYear('ts'))
  elif model_name == _LOG_REV:    
    qs = LogReversal.objects.using('billing').values(year=ExtractYear('ts'))
  elif model_name == _TRX:
    qs = Payment.objects.using('billing').values(year=ExtractYear('ts'))

  qs = qs.annotate(count_year=Count('year')).order_by('-year');
  print('> get_years_from_records %s = %s ' % (model_name, qs))
    
  return qs

def iterate_log(list_years, qs_all):
  print('> iterate_log %s = %s ' % (list_years, qs_all.model))
  
  ret = []
  for item in list_years:
    temp_arr = {}
    cyear = item['year']

    qs = qs_all.filter(ts__year=cyear)
    # print (qs)

    count_all = qs.count()
    count_success = qs.filter(rc = '00').count()
    count_failed = qs.filter(~Q(rc = '00')).count()

    count_success_percent = percentage(count_success, count_all)
    count_failed_percent = percentage(count_failed, count_all)

    temp_arr['year'] = cyear
    temp_arr['total'] = count_all
    temp_arr['total_success'] = count_success
    temp_arr['total_failed'] = count_failed
    temp_arr['total_success_percent'] = count_success_percent
    temp_arr['total_failed_percent'] = count_failed_percent

    ret.append(temp_arr)
  
  return ret

from django.db.models import Q
def get_summary_log(model):
  ret = None
  if model == _LOG_INQ:
    list_years = get_years_from_records(_LOG_INQ)
    qs = LogInquiry.objects.using('billing').all()

  elif model == _LOG_PAY:
    list_years = get_years_from_records(_LOG_PAY)
    qs = LogPayment.objects.using('billing').all()

  elif model == _LOG_REV:
    list_years = get_years_from_records(_LOG_REV)
    qs = LogReversal.objects.using('billing').all()
  
  elif model == _TRX:
    list_years = get_years_from_records(_TRX)
    qs = LogReversal.objects.using('billing').all()

  ret = iterate_log(list_years, qs)
  print (ret)

  return ret