FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

EXPOSE 8000

WORKDIR /usr/src/app

# ## Add certificates if SSL error    
# COPY pl.crt /usr/local/share/ca-certificates/
# ## In windows, Run -> Manage computer certificates -> Trusted Root Certification Authorities -> Certificates -> Cisco Umbrella Root CA -> Details -> Copy to File... -> Base-64 Encoded...
# COPY cisco.pem /usr/local/share/ca-certificates/
# # RUN update-ca-trust extract
# RUN update-ca-certificates
# RUN for FX in /usr/local/lib/python3.7/site-packages/pip/_vendor/*/cacert.pem; do \
# echo "installing to $FX" ; \
# cat /usr/local/share/ca-certificates/cisco.pem >> $FX ; \
# cat /usr/local/share/ca-certificates/pl.crt >> $FX ; \
# done


COPY requirements.txt /usr/src/app/requirements.txt

RUN python3 -m pip install -r requirements.txt --proxy=avproxy.pacificlife.net:8080 --trusted-host pypi.org --trusted-host files.pythonhosted.org

COPY app/ /usr/src/app/

# CMD uvicorn serve_model:app --host 0.0.0.0 --port 80