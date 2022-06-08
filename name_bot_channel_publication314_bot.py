
def save_modern (namebot,user_id,name):
    import iz_telegram
    tovar_id = iz_telegram.save_tovar (user_id,namebot,name,'','Модерация','')
    return tovar_id
          
def mesage_list (namebot,user_id,sql,message_list,message_no):          
    import iz_func
    import iz_telegram
    db,cursor = iz_func.connect ()    
    cursor.execute(sql)
    data = cursor.fetchall()
    list_tovar = []
    for rec in data: 
        id,name = rec.values()
        list_tovar.append([id,name])
    if list_tovar == []:
        message_out = iz_telegram.list_tovar (user_id,namebot,list_tovar,message_list,'del','')
    else:    
        message_out = iz_telegram.list_tovar (user_id,namebot,list_tovar,message_list,'del','')
    return message_out      
          
def start_prog (user_id,namebot,first_name,last_name,username,is_bot,language_code,status,message_id,name_file_picture,telefon_nome,refer,FIO_id,lastid_log,message_in,message_old,user_id_refer):
    import iz_func
    import iz_telegram 
    currency = 'Валюта бота'
    
    if status == 'Добавить канал':
        name = message_in
        save_modern (namebot,user_id,name)
    
    if message_in == 'Настройки':
        message_out,menu = iz_telegram.get_message (user_id,'Настройки пользователя',namebot)
        balans = iz_telegram.get_balans (user_id,namebot,currency)
        message_out = message_out.replace('%%Баланс%%',str(balans))        
        markup = ''
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)  
        
    if message_in == '🖋️Каналы на модерации':
        sql = "select id,name from bot_product where namebot = '"+str(namebot)+"' and parameter02 = 'Модерация' limit 100"
        message_out =  mesage_list (namebot,user_id,sql,'Список товаров на модерации','У вас нет подключенных каналов')
        markup = ''
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0) 

    if message_in == '📒Мои каналы':
        sql = "select id,name from bot_product where namebot = '"+str(namebot)+"' and parameter02 = 'Рабочий' limit 100"
        message_out =  mesage_list (namebot,user_id,sql,'Список каналов','Вы еше не указали канал')
        markup = ''
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0) 
      
      
      
      
    if message_in.find ('info') != -1:
        import json
        json_string  = iz_func.change_back(message_in.replace('info_',''))
        data_json = json.loads(json_string)
        operation = data_json['o']

        if operation == 'send':
            id_doctor   = data_json['id_doctor']
            print ('[+] id_doctor',id_doctor)
            
            list_doctor = list_send (namebot,select_doctor (namebot,id_doctor))
            print ('[+] list_doctor',list_doctor)
            for send_user in list_doctor:
                markup = ''
                answer = iz_telegram.bot_send (send_user[1],namebot,"Приглашение доктору",markup,0) 
            
            
