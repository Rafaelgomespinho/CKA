FROM debian

LABEL app="Teste meu primeiro dockerfile"
ENV Teste="Salve"

RUN apt-get update && apt-get install -y nginx && apt-get install -y stress

CMD echo "Salve teste do CMD e nois"
