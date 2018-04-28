%Ficha pl3
%exercicio 1.1
close all
clear all
%--ler ficheiro com as series temporais
load seriestemp.dat % seriestemp.dat e um ficheiro ASCII
x=seriestemp; %series temporais
x1=seriestemp(:,1); %serie temporal 1
x2=seriestemp(:,2); %serie temporal 2
N=length(x); %comprimento das series temporais
t=(0:N-1)'; %escala temporal
% representaçção grafica
figure(1)
subplot(211) % duas linha e uma coluna e coloca no primeiro espaço
plot(t,x1,'+-');
legend('serie temporal 1','Location','northwest')
xlabel('t[h]');
title('series temporais');
subplot(212)
plot(t,x2,'+-');
legend('serie temporal 2','Location','northwest')
xlabel('t[h]');

%ex 1.2
%verifica a existencia de Nan
disp('há NaN?')
haNaN=any(isnan(x)) %ha NaN por colunas?
colNaN=find(isnan(x)) %colunas com Na

% elimina linhas com NaN e reconstroi

x1r=x1;
if any(isnan(x1))
    ind=find(isnan(x1));
    for k=1:length(ind)
        tt=t(ind(k)-4:ind(k)-1);
        xx=x1r(ind(k)-4:ind(k)-1);
        x1r(ind(k))=interp1(tt,xx,t(ind(k)),'pchip','extrap')
    end
end
x2r=x2;
if any(isnan(x2))
    ind2=find(isnan(x2));
    for k=1:length(ind2)
        tt2=t(ind2(k)-4:ind2(k)-1);
        xx2=x2r(ind2(k)-4:ind2(k)-1);
        x2r(ind2(k))=interp1(tt2,xx2,t(ind2(k)),'pchip','extrap')
    end
end
   


% representaçção grafica
figure(2)
subplot(211) % duas linha e uma coluna e coloca no primeiro espaço
plot(t,x1r,'-');
legend('serie temporal 1','Location','northwest')
xlabel('t[h]');
title('series temporais');
subplot(212)
plot(t,x2r,'-');
legend('serie temporal 2','Location','northwest')
xlabel('t[h]');

%calcular a media
media=mean(x1r)
media2=mean(x2r)
%calcular a desvio padrao
desvio1=(std(x1r));
desvio2=std(x2r)
%calcular a correlaçao
correlacao=corrcoef(x1r,x2r)

%1.4 Eliminação de outliers
max1=media+(3*desvio1)
max2=media2+(3*desvio2)
min1=media-(3*desvio1)
min2=media2-(3*desvio2)

for i=1:length(x1r)
    if x1r(i)>max1
        x1r(i)=media+(2.5*desvio1)
    elseif x1r<min1
            x1r(i)=media-(2.5*desvio1)
        end
end
for i=1:length(x2r)
    if x2r(i)>max2
        x2r(i)=media2+(2.5*desvio2)
    elseif x2r<min2
            x2r(i)=media2-(2.5*desvio2)
        end
end

figure(3)
subplot(211) % duas linha e uma coluna e coloca no primeiro espaço
plot(t,x1r,'+-');
legend('serie temporal 1','Location','northwest')
xlabel('t[h]');
title('series temporais');
subplot(212)
plot(t,x2r,'+-');
legend('serie temporal 2','Location','northwest')
xlabel('t[h]');% this works

save seriestemp_reg.mat x1r x2r t
