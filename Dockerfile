FROM ubuntu:latest

COPY dist .

ENV LINK_ENV="${LINK_ENV}"

CMD ["./dist/main.exe", "$LINK_ENV"]