% Aplicação à série x1ro

%--- EX1.1: Ler ficheiro com as séries temporais regularizadas
load seriestemp_comp.mat
% x1r - série temporal 1 regularizada
% x2r - série temporal 2 regularizada
N=length(x1r); %Comprimento de cada série temporal
t = (0:N-1)'; %escala temporal
tt=(0:2*N-1)'; %escala temporal para previsão

%---------Ex 1.2-------------
adftest(x1r) %teste de estacionaridade da série regularizada
adftest(st1) %teste de estacionaridade da componente sazonal

%---------Ex 1.3-------------
t1=(0:23)';
y1=st1(1:24); %componente sazonal
figure(1)
subplot(211)
autocorr(y1) %indicador para a ordem de nc(modelo MA)
subplot(212)
parcorr(y1) %indicador para a ordem de na(modelo AR)

%---------Ex 1.4-------------
id_y1 = iddata(y1, [], 1, 'TimeUnit', 'hours');

%---------Ex 1.5-------------
opt1_AR = arOptions('Approach', 'ls');
na1_AR=6; %histórico da variável
model1_AR = ar(id_y1,na1_AR, opt1_AR); %modelo AR
pcoef1_AR = polydata(model1_AR); %parâmetros do modelo AR

%---------Ex 1.6-------------
%Simulação do modelo AR
y1_AR = y1(1:na1_AR);
for k=na1_AR+1:24,
    y1_AR(k)=sum(-pcoef1_AR(2:end)'.*flip(y1_AR(k-na1_AR:k-1)));
end
y1_AR2=repmat(y1_AR,2,1);

%Simulação do modelo AR com forecast
y1_ARf=forecast(model1_AR,y1(1:na1_AR),24-na1_AR);
y1_ARf2=repmat([y1(1:na1_AR); y1_ARf],2,1);

%----------Ex 1.7------------
figure(2)
plot(t,st1,'-+',t,y1_AR2,'-o',t,y1_ARf2,'-*');
xlabel('t [h]');
title('Componente sazonal 1 (-+) e estimação com modelo AR');

figure(3)
plot(t,x1r,'-+',t,y1_AR2, tr1_2,'-o');
xlabel('t [h]');
title('Série 1(-+) e estimação com o modelo AR(-o)');

%Métrica para análise
E1_AR=sum((x1r-(y1_AR2+tr1_2)).^2)

%----------Ex 1.8-------------
tr1_2_2=polyval(p1,tt); %Calcula tendência para 2N

figure(4)
plot(t,x1ro,'-+',tt,repmat(y1_AR2,2,1)+tr1_2_2,'-o');
xlabel('t [h]');
title('Série 1 (-+) e Previsão com o modelo AR (-o)');

%----------Ex 1.9-------------
% Estimação de um modelo arma

opt1_ARMAX = armaxOptions('SearchMethod', 'auto');
na1_ARMA=5;
nc1_ARMA=1;
model1_ARMA = armax(id_y1,[na1_ARMA nc1_ARMA], opt1_ARMAX);
[pa1_ARMA,pb1_ARMA,pc1_ARMA] = polydata(model1_ARMA);

%----------Ex 1.10------------
e = randn(24,1); %ruído branco

y1_ARMA = y1(1:na1_ARMA);
for k=na1_ARMA+1:24,
    y1_ARMA(k)=sum(-pa1_ARMA(2:end)'.*flip(y1_ARMA(k-na1_ARMA:k1)))+sum(pc1_ARMA'.*flip(e(k-nc1_ARMA:k)));
end
y1_ARMA2=repmat(y1_ARMA,2,1);

%Simulação do modelo arma com forecast
y1_ARMAf=forecast(model1_ARMA, y1(1:na1_ARMA),24-na1_ARMA);
y1_ARMAf2=repmat([y1(1:na1_ARMA); y1_ARMAf],2,1);

%-----------Ex 1.11------------
figure(5) %compara a componente sazonal com a sua estimação
plot(t,st1,'-+',t,y1_ARMA2,'-o',t,y1_ARMAf2,'-*');
xlabel('t [h]');
title('Componente sazonal 1(-+) e estimação com o modelo ARMA');

figure(6) %compara a série com o modelo ARMA + tendência
plot(t,x1r,'-+',t,y1_ARMA2+tr1_2,'-o');
xlabel('t [h]');
title('Série 1 (-+) e estimação com o modelo ARMA(-o)')

%Métrica para análise
E1_ARMA = sum((x1r-y1_ARMA2(1:N)).^2)

%-----------Ex 1.12------------
figure(7) %Faz a previsão para 2N
plot(t,x1r,'-+',tt,repmat(y1_ARMA2,2,1)+tr1_2_2, '-o');
xlabel('t [h]');
title('Série 1(-+) e previsão com o modelo ARMA(-o)')

%-----------Ex 1.13-------------
%Estimação de um modelo ARIMA
EstMd1 = estimate(Md,x1r(1:N), 'Y0', x1r(1:p1_ARIMA+1));

%-----------Ex 1.14-------------
%Simulação do modelo ARIMA
y1_ARIMA = simulate(EstMd1,N);

%-----------Ex 1.15-------------
figure(8) %compara a serie com a sua estimaçao
plot(t,x1r,'-+',t,y1_ARIMA,'-o');
xlabel('t [h]');
title('Série 1(-+) e estimação com o modelo ARIMA(-o)')

%métrica para análise
E1_ARIMA=sum((x1r-y1_ARIMA(1:N)).^2)

%-----------Ex 1.16--------------
%Simulação do modelo ARIMA para 2N
y1_ARIMA2 = simulate(EstMd1,2*N);

figure(9) %faz a previsão para 2N
plot(t,x1r,'-+',tt,y1_ARIMA2,'-o');
xlabel('t [h]');
title('Série 1(-+) e estimação com o modelo ARIMA(-o)')