cert_issuer=$(openssl x509 -noout -in input.txt -issuer)
cert_subject=$(openssl x509 -noout -in input.txt -subject)
issuer=$(echo $cert_issuer | sed 's/issuer=[[:blank:]]//')
subject=$(echo $cert_subject | sed 's/subject=[[:blank:]]//')
if [[ $issuer = $subject ]]
then
        echo "1" > output.txt
else
        echo "0" > output.txt
fi