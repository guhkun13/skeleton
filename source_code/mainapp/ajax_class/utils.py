from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from mainapp.ajax_class.log_inquiry import LogInquiryClass
from mainapp.ajax_class.log_payment import LogPaymentClass
from mainapp.ajax_class.log_reversal import LogReversalClass
from mainapp.ajax_class.trx import TrxClass
from mainapp.ajax_class.mapping_biller import MappingBillerClass

def get_model_class(model):
    if model == 'your_model_name':
        result = YourClassModel()
    elif model == 'log_inquiry':
        result = LogInquiryClass()
    elif model == 'log_payment':
        result = LogPaymentClass()
    elif model == 'log_reversal':
        result = LogReversalClass()
    elif model == 'trx':
        result = TrxClass()
    elif model == 'mapping_biller':
        result = MappingBillerClass()

    return result

def process_params(datatables):
    order_idx = int(datatables.get('order[0][column]'))
    order_dir = datatables.get('order[0][dir]')
    order_col = 'columns[' + str(order_idx) + '][data]'
    order_col_name = datatables.get(order_col)

    if (order_dir == "desc"):
        order_col_name =  str('-' + order_col_name)

    result = {}
    result['draw'] = int(datatables.get('draw'))
    result['start'] = int(datatables.get('start'))
    result['length'] = int(datatables.get('length'))
    result['search'] = datatables.get('search[value]')
    result['order_col_name'] = order_col_name

    return result

def process_paginator(datas, start, length):
    paginator = Paginator(datas, length)
    page_number = start / length + 1

    try:
        object_list = paginator.page(page_number).object_list
    except PageNotAnInteger:
        object_list = paginator.page(1).object_list
    except EmptyPage:
        object_list = paginator.page(1).object_list

    return object_list

def filter_specific_column(datas, datatables):
    idx=0
    for itemcol in datatables:
        colname = 'columns['+str(idx)+'][data]'
        colsearchval = 'columns['+str(idx)+'][search][value]'

        colname = datatables.get(colname)
        colsearchval = datatables.get(colsearchval)
        if (colsearchval):
            search_type = 'icontains'
            filter = colname + '__' + search_type
            datas=datas.filter(**{ filter: colsearchval })

        idx+=1

    return datas
