# 1secmail
1secmail api library
# Requirements

python 3.x
'''
  pip install requests
'''
# Usage
  1-generate bunch of random temp-emails
  '''
  import secmail.secmail as sec
  email_list = sec.generate_email(10)
  '''
  
  2- get's last inbox mail from one of generated temp-emails
  '''
  import secmail.secmail as sec
  email = "demo@secmail.com"
  id = sec.id_mailinbox(mail=email)[0]
  '''
  
  3- get's information of latest inboxed mail
  '''
  import secmail.secmail as sec
  email = "demo@secmail.com"
  id = sec.id_mailinbox(mail=email)[0]
  subject,email,content = sec.email_content(mail=email,id=id,html=False)
  '''
  
  
  see the api reference [here](https://www.1secmail.com/api/)
