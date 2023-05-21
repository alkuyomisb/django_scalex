import mysql.connector
import matplotlib.pyplot as plt

def get_all_plans ():
    plans = []
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="scalex"
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM plan")
    myresult = mycursor.fetchall()

    for plan in myresult:
        p = record_to_dict(plan)
        plans.append(p)
    

   
    mydb.close()
    return plans


def get_plans(**conditions):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="scalex"
    )

    query_conditions = ""

    for index, condition in enumerate(conditions):
        if conditions[condition] == "all":
            continue

        if index != 0:
            query_conditions += " AND "
        else:
            query_conditions += " WHERE "

        query_conditions += "{} = '{}'".format(
            condition, conditions[condition])

    query = "SELECT * FROM plan {} ;".format(query_conditions)
    print(query)
    cursor = db.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    plans = []
    

    for index, record in enumerate(records):
        data = {
            "price_value": record[1],
            "price_unit": record[2],
            "data_allowance_value": record[3],
            "data_allowance_unit": record[4],
            "flexi_minutes": record[5],
            "local_minutes": record[6],
            "international_minutes": record[7],
            "duration_value": record[8],
            "duration_unit": record[9],
            "isp": record[10],
            "link": record[11],
            "social_media_data_value": record[12],
            "social_media_data_unit": record[13],
            "last_checked ": record[14],
            "status": record[15],
            "service_type": record[16],
            "plan_type": record[17],
            "title": record[18],
            "sms": record[19],
            "download_speed_value": record[20],
            "download_speed_unit": record[21],
            "upload_speed_value": record[22],
            "upload_speed_unit": record[23],
            "fixed_line_minutes": record[24],
            "world_roaming_value": record[25],
            "world_roaming_unit": record[26],
            "contract_duration_value": record[27],
            "contract_duration_unit": record[28],
            "add_on_link": record[29]
        }
        plans.append(data)
    db.close()
    return plans


def get_one_closest(filter_dict, orders_by_dict, limit):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="scalex"
    )

    # Conditions
    query_conditions = ""
    for index, condition in enumerate(filter_dict):
        if filter_dict[condition] == "all":
            continue

        if index != 0:
            query_conditions += " AND "
        else:
            query_conditions += " WHERE "

        query_conditions += "{} = '{}'".format(
            condition, filter_dict[condition])

    # Order By
    query_orders_by = ""
    query_distances = ""
    for index, order_by in enumerate(orders_by_dict):
        query_distances += " , abs({} - {}) as distance_from_{} ".format(
            order_by, orders_by_dict[order_by], order_by)
        if index != 0:
            query_orders_by += " , distance_from_{} ".format(order_by)
        else:
            query_orders_by += "distance_from_{} ".format(order_by)

    query = """
            SELECT   *
            {}
            FROM  plan
            {}
            ORDER BY {}
            LIMIT 0,{}
            """.format(query_distances, query_conditions, query_orders_by, limit)

    cursor = db.cursor()
    cursor.execute(query)
    if limit == 1:
        record = cursor.fetchone()
        if cursor.rowcount == 0:
            return get_empty_dict()
        data = record_to_dict(record)
        db.close()
        return data
    else:
        records = cursor.fetchall()
        data_list = []
        print(data_list)
        print("______________________________________________________________________")

        for record in records:
            data = record_to_dict(record)
            # print(data)
            data_list.append(data)
            print(data_list)
            print("TYPE: " + str(type(data_list)))
            print(
                "______________________________________________________________________")

        db.close()
        return data_list


def record_to_dict(record):
    data = {
        "price_value": record[1],
        "price_unit": record[2],
        "data_allowance_value": record[3],
        "data_allowance_unit": record[4],
        "flexi_minutes": record[5],
        "local_minutes": record[6],
        "international_minutes": record[7],
        "duration_value": record[8],
        "duration_unit": record[9],
        "isp": record[10],
        "link": record[11],
        "social_media_data_value": record[12],
        "social_media_data_unit": record[13],
        "last_checked ": record[14],
        "status": record[15],
        "service_type": record[16],
        "plan_type": record[17],
        "title": record[18],
        "sms": record[19],
        "download_speed_value": record[20],
        "download_speed_unit": record[21],
        "upload_speed_value": record[22],
        "upload_speed_unit": record[23],
        "fixed_line_minutes": record[24],
        "world_roaming_value": record[25],
        "world_roaming_unit": record[26],
        "contract_duration_value": record[27],
        "contract_duration_unit": record[28],
        "add_on_link": record[29]
    }
    return data


def get_empty_dict():
    data = {
        "price_value": "-",
        "price_unit": "-",
        "data_allowance_value": "-",
        "data_allowance_unit": "-",
        "flexi_minutes": "-",
        "local_minutes": "-",
        "international_minutes": "-",
        "duration_value": "-",
        "duration_unit": "-",
        "isp": "-",
        "link": "-",
        "social_media_data_value": "-",
        "social_media_data_unit": "-",
        "last_checked ": "-",
        "status": "-",
        "service_type": "-",
        "plan_type": "-",
        "title": "-",
        "sms": "-",
        "download_speed_value": "-",
        "download_speed_unit": "-",
        "upload_speed_value": "-",
        "upload_speed_unit": "-",
        "fixed_line_minutes": "-",
        "world_roaming_value": "-",
        "world_roaming_unit": "-",
        "contract_duration_value": "-",
        "contract_duration_unit": "-",
        "add_on_link": "-"
    }
    return data

def add_chart(chartType , xAxis , yAxis):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="scalex"
    )

    cursor = db.cursor()
    cursor.execute("INSERT INTO charts (chartType ,xAxis , yAxis) values ('{}' , '{}' , '{}');".format(chartType ,xAxis , yAxis))
    


def get_axis_list(axis , isFloat = False):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="scalex"
    )
    axis_list = []
    
    cursor = db.cursor()
    cursor.execute("SELECT id, {} FROM plan".format(axis))
    plans_tale = cursor.fetchall()
    for axis in plans_tale:
        id = axis[0]
        value = axis[1]
        value = ''.join(filter(lambda x: x.isdigit() or x == '.', str(value)))
        if value == '':
            value = '0'
        axis_list.append(value)
        if isFloat:
            axis_list.append(float(value))
        else:
            axis_list.append(value)



    return axis_list

def get_all_charts ():
    all_charts = []
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="scalex"
    )

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM charts")
    charts = cursor.fetchall()

    for chart in charts:
        all_charts.append(chart)
    
    mydb.close()
    return all_charts

def get_chart_dict():
   db_charts = get_all_charts()
   res = {"charts" : []}
   try:
    for chart in db_charts:
            chart_dict = {"xAxis_list" : [], "yAxis_list" : [], "xAxis_lable" : "" , "yAxis_lable" : "","chartType" : ""}
            xAxis_list = get_axis_list(chart[1] ,isFloat=True)
            yAxis_list = get_axis_list(chart[2] ,isFloat=True)
            xAxis_lable = chart[1]
            yAxis_lable = chart[2]
            chartType = chart[3]
            chart_dict["xAxis_list"] = xAxis_list
            chart_dict["yAxis_list"] = yAxis_list
            chart_dict["xAxis_lable"] = xAxis_lable
            chart_dict["yAxis_lable"] = yAxis_lable
            chart_dict["chartType"] = chartType

            res["charts"].append(chart_dict)
   except NameError:
    pass



   return res





    














    
    
    
   
