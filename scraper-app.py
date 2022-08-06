from requests_html import HTMLSession
import pandas as pd

session = HTMLSession()

header ={
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
role=input('Veuiller entrer votre role: ')
endpage=int(input('Veuiller le nombre de page que vous voulez analyser: '))
data = []
urls=['https://ma.indeed.com/jobs?q={}&l=maroc&start={}'.format(role,x) for x in range(10, endpage, 10)]
for url in urls:
	r=session.get(url.strip(),headers=header)
	job_content=r.html.find('div.job_seen_beacon')
	#print(job_content)
	for job in job_content:
		try:
			label = job.find('span.label.css-1qj35nq.eu4oa1w0' , first=True).text
		except:
			label= ''
		#print(label)
		try:
			title_job = job.find('span[title]' , first=True).text
		except:
			title_job= ''
		#print(title_job)
		try:
			company_name = job.find('span.companyName' , first=True).text
		except:
			company_name= ''
		#print(company_name)
		try:
			Location_company = job.find('div.companyLocation' , first=True).text
		except:
			Location_company= ''
		#print(Location_company)
		try:
			date_of_post = job.find('span.date' , first=True).text.replace('il y a ', '')
		except:
			date_of_post= ''
		try:
			summary = job.find('div.job-snippet' , first=True).text
		except:
			summary= ''
        try:
			type_of_job = job.find('div.metadata' , first=True).text
		except:
			type_of_job= ''
		#print(date_of_post)
		dic = {
            'Label':label,
            'Title_job':title_job,
            'Company_Name':company_name,
            'Location_Company':Location_company,
            'Date_Of_Post':date_of_post,
            #'Summary':summary
            'type':type_of_job
		}

		data.append(dic)
df=pd.DataFrame(data)
df.to_csv('results.csv')
print('Completed')