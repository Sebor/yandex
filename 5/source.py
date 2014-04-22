__author__ = 'Sebor'
import subprocess
def SSLcert(cert):
	try:
		cert_issuer = subprocess.check_output(["openssl", "x509", "-noout", "-in", cert, "-issuer"], stderr=subprocess.STDOUT).decode()
		cert_subject = subprocess.check_output(["openssl", "x509", "-noout", "-in", cert, "-subject"], stderr=subprocess.STDOUT).decode()
		issuer = cert_issuer.split("=")[-1]
		subject = cert_subject.split("=")[-1]
		Output = open('output.txt', 'w')
		if issuer == subject:
				Output.write('1')
		else:
				Output.write('0')
		Output.close()
	except subprocess.CalledProcessError:
		print ('Something wrong')
SSLcert('input.txt')