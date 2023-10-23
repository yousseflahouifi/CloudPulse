# CloudPulse - AWS Cloud Landscape Search Engine
During the reconnaissance phase, an attacker searches for any information about his target to create a profile that will later help him to identify possible ways to get in an organization.
<br>
CloudPulse is a powerful tool that simplifies and enhances the analysis of SSL certificate data. It leverages the extensive repository of SSL certificates obtained from the AWS EC2 machines available at [Trickest Cloud](https://github.com/trickest/cloud). With CloudPulse , security researchers can efficiently explore SSL certificate details, uncover potential vulnerabilities, and gather valuable insights for a variety of security-related tasks.

# Architecture and how it works
<img src="https://github.com/yousseflahouifi/CloudPulse/blob/main/cp.png" alt="cloudpulse" width="100%">
<br>

# How can it benefit you 

Simplifies security assessments with a user-friendly interface. It allows you to effortlessly find company's asset's on aws cloud:

- IPs
- subdomains
- domains associated with a target
- organization name
- discover origin ips

 # 🛠️ Installation
 ### Method 1 :
 1- Download CloudPulse :
```
git clone https://github.com/yousseflahouifi/CloudPulse
cd CloudPulse/
```

2- Run docker compose :
```
docker-compose up -d
```

3- Run script.py script
```
docker-compose exec web python script.py
```

 4 - Now go to http://<ip>:8000/search and enjoy the search engine
### Method 2 :
 1- download CloudPulse :
```
git clone https://github.com/yousseflahouifi/CloudPulse
cd CloudPulse/
```
2- Setup virtual environment :
```
python3 -m venv myenv
source myenv/bin/activate
```
3- Install requirements.txt file : 
```
pip install -r requirements.txt
```

4- run an instance of elasticsearch using docker :
```
docker run -d --name elasticsearch -p 9200:9200 -e "discovery.type=single-node" elasticsearch:6.6.1
```
5- update script.py and settings file to the host 'localhost':
```
#script.py
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
```

```
#se/settings.py

ELASTICSEARCH_DSL = {
    'default': {
        'hosts': 'localhost:9200'
    },
}
```
6- Run script.py to index data in elasticsearch:
```
python script.py
```

7- Run the app:
```
python manage.py runserver 0:8000
```




 # ⚠️ Important notes
 Included in the CloudPulse repository is a sample data.csv file containing close to 4,000 records, which provides a glimpse of the tool's capabilities. For the full dataset, visit the [Trickest Cloud](https://github.com/trickest/cloud) repository clone the data and update data.csv file (it contains close to 9 millions data)

# Example :
as an example searching for .mil data gives:
<br>
<img src="https://github.com/yousseflahouifi/CloudPulse/blob/main/cloudpulse.jpg" alt=".mil data" width="50%">

searching for tesla as en example gives :

<br>
<img src="https://github.com/yousseflahouifi/CloudPulse/blob/main/teslademo.png" alt="tesla demo" width="50%">

# Limitations :
CloudPulse heavily depends on the data.csv file, which is a sample dataset extracted from the larger collection maintained by Trickest. While the sample dataset provides valuable insights, the tool's full potential is realized when used in conjunction with the complete dataset, which is accessible in the Trickest repository [here](https://github.com/trickest/cloud).
<br>
Users are encouraged to refer to the Trickest dataset for a more comprehensive and up-to-date analysis.
# References:
- [Scan aws ip ssl certificates](https://www.daehee.com/scan-aws-ip-ssl-certificates/)
- [Trickest cloud dataset](https://github.com/trickest/cloud)
- [cloud provider infrastructure mapping](https://trickest.com/blog/cloud-provider-infrastructure-mapping/)
- [Sam Erb - Hunting Certificates and Servers - DEF CON 27 Packet Hacking Village](https://www.youtube.com/watch?v=1pqCqz3JzXE)
