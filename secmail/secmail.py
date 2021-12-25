''' Python package for 1secmail.com
    to generate and manage generated
    temp mails.
'''
import requests as req
import json
def generate_email(n:int = 1):
    '''
    :Use: this function takes one arguments.
    it generates n emails by the api.
    return: a list of new-generated e-mails
    '''
    first_ = "https://www.1secmail.com/api/v1/?action=genRandomMailbox&count={0}"
    emails_list = json.loads(req.get(first_.format(str(n))).text)

    return emails_list


def id_mailinbox(mail:str):
    '''
    :param mail: an mail generated from 1secmail using
    generate_email func.
    :return: email's id as an int, resp list oject
    '''
    second_ = 'https://www.1secmail.com/api/v1/?action=getMessages&login={0}&domain={1}'
    login,domain = mail.split("@")
    resp = json.loads(req.get(second_.format(login,domain)).text)
    '''
    the incoming resp will be a string. json.loads will convert
    it to a dictionaries list 
    '''
    id = int(resp[0]["id"])
    '''
    Note:
        the resp may contain many mails but this method only 
        returns id of the last inboxed mail. if you need a 
        different id you can export it from resp list.
    '''
    
    return id,resp


def email_content(mail:str,id:int, html:bool = False):
    '''
    :param id: mail's id
           mail: generated email from 1secmail.
           html: boolean.
    :Note:
        you can get it from id_mailinbox func.
    :return: mail-subject as a string.
             mail-sender.
             content as HTML or Text.
    '''
    third_ = 'https://www.1secmail.com/api/v1/?action=readMessage&login={0}&domain={1}&id={2}'
    login,domain = mail.split("@")
    id = str(id)
    response = json.loads(req.get(third_.format(login,domain,id)).text)
    sender = response["from"]
    subject = response["subject"]
    if html: content = response["htmlBody"]
    else: content = response["textBody"]
        
    return  subject,sender,content

