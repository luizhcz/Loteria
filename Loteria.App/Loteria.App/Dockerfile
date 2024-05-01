# Define a imagem base usando o SDK do .NET 7.0 para o processo de build.
FROM mcr.microsoft.com/dotnet/sdk:7.0 AS build-env
WORKDIR /app

# Copie o arquivo csproj e restaure as dependências necessárias.
COPY *.csproj ./
RUN dotnet restore

# Copie o restante dos arquivos do projeto para o diretório de trabalho.
COPY . ./

# Publique a aplicação com configuração de Release.
RUN dotnet publish -c Release -o out

# Use a imagem base do runtime do .NET 7.0 para a imagem final.
FROM mcr.microsoft.com/dotnet/aspnet:7.0
WORKDIR /app

# Copie os arquivos publicados do estágio de build para o estágio de runtime.
COPY --from=build-env /app/out .

# Defina o ponto de entrada para iniciar a aplicação.
ENTRYPOINT ["dotnet", "Loteria.App.dll"]
