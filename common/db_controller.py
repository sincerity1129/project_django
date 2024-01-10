def db_create(table, **create_columns):
    query_result = table.objects.create(**create_columns)
    return query_result  

def db_filter(table, **filter_columns):
    query_result = table.objects.filter(**filter_columns)
    return query_result    

def db_update(table, filter_query, **update_columns):
    table.objects.filter(**filter_query).update(**update_columns)

def db_delete(table, **delete_columns):
    table.objects.filter(**delete_columns).delete()

def db_exclude(table, **exclude_columns):
    query_result = table.objects.exclude(**exclude_columns)
    return query_result    
    
def all_db_search(table):
    query_result = table.objects.all()
    return query_result