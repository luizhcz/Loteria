# Use a imagem oficial do SDK do .NET para compilar o código em um ambiente isolado.
FROM mcr.microsoft.com/dotnet/sdk:7.0 AS build-env
WORKDIR /app

# Copie os arquivos csproj e restaure as dependências identificadas
COPY *.csproj ./
RUN dotnet restore

# Copie o restante dos arquivos do projeto e construa a aplicação
COPY . ./
RUN dotnet publish -c Release -o out

# Gere a imagem final, usando a imagem de runtime do .NET para reduzir o tamanho
FROM mcr.microsoft.com/dotnet/aspnet:7.0
WORKDIR /app
COPY --from=build-env /app/out .
ENTRYPOINT ["dotnet", "Loteria.App.dll"]