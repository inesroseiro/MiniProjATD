clear all
close all
load seriestemp_reg.mat
%1.1
figure(1)
subplot(211) % duas linha e uma coluna e coloca no primeiro espaço
plot(t,x1r,'+-');
legend('serie temporal 1','Location','northwest')
xlabel('t[h]');
title('series temporais');
subplot(212)
plot(t,x2r,'+-');
legend('serie temporal 2','Location','northwest')
xlabel('t[h]');

%1.2
    %grau1
x1d=detrend(x1r)
x2d=detrend(x2r)
figure(2)
subplot(211) % duas linha e uma coluna e coloca no primeiro espaço
plot(t,x1d,'+-');
legend('serie temporal 1','Location','northwest')
xlabel('t[h]');
title('series temporais');
subplot(212)
plot(t,x2d,'+-');
legend('serie temporal 2','Location','northwest')
xlabel('t[h]');


%correção do professor
 figure(3)
 plot(t,x1d,'+-',t,x2d,'*-');
 legend('serie 1 regularizada','serie 2 regularizada','Location','northwest')
 xlabel('t[h]');
%correçao do professor
x1ro_t0=detrend(x1r,'constant');%media da serie, grau 0
t1r_0=x1r-x1ro_t0;
x1ro_t1=detrend(x1r,'linear');%serie sem tendencia, grau 1
t1r_1=x1r-x1ro_t1; 
x2r_t0=detrend(x2r,'constant');
tr2_t0=x2r-x2r_t0; 
x2r_t1=detrend(x2r,'linear');
tr2_1=x2r-x2r_t1; 

%1.4
figure(4)
subplot(211)
plot(t,x1r,'-.',t,t1r_0,'+-');
title('serie 1 (+) e trend (*) de grau 0')
 xlabel('t[h]');
 
 figure(5)
 subplot(211)
 plot(t,x2r,'+-',t,tr2_t0,'*-');
 title('serie 2 (+) e trend (*) de grau 0')
 xlabel('t[h]');
 
 subplot(212)
 plot(t,x1ro_t1,'o-');
  xlabel('t[h]');


figure(6)
subplot(211)
plot(t,x2r,'-+',t,tr2_1,'-*');
title('serie e + trend * grau 1')
 xlabel('t[h]');
 subplot(212)
 plot(t,x2r_t1,'-o');
 title('sere 2 sem (o) trend grau 1')
  xlabel('t[h]');
  
  %1.5 1.6 1.7
 disp('aproximaçao linear de grau 2:')
 p1=polyfit(t,x1r,2) %coeficientes dos polinomios
 p2=polyfit(t,x2r,2)
 p12=polyval(p1,t) %valores resultantes
 p22=polyval(p2,t)
 x1ro_t2=x1r-p12;
 x2ro_t2=x2r-p22;
 figure(7)
 subplot(411)
 plot(t,x1r,'-*',t,p12,'-*');
 title('serie 1 + trend de grau 2')
 subplot(412)
 plot(t,x1ro_t2);
 title('serie 1 sem trend de grau 2')
 
 subplot(413)
 plot(t,x2r,'-*',t,p22,'-*');
 title('serie 2 + trend de grau 2')
 xlabel('t[h]')
 subplot(414)
 plot(t,x2ro_t2);
 title('serie 2 sem trend de grau 2')
 
 
 % 1.8 1.19
 ho=repmat([1:24]',2,1); %assumindo sazonalidade de 24h
 sX=dummyvar(ho); %gera matriz dummy
 Bs1=sX\x1ro_t1;%obtem valores para cada 24h
 st1=sX*Bs1;%componente sazonal´
 
 Bs2=sX\x2ro_t2;%ontem valores para cada 24h
 st2=sX*Bs2;%compente sazonal
 x1ro_s=x1r-st1;
 x2ro_s=x2r-st2;
 % 1.10
 figure(8)
 subplot(211)
 plot(t,x1r,'-+',t,x1ro_s,'-o');
 title('serie 1 (+) e sem sazonalidade (o)')
 subplot(212)
 plot(t,st1,'*-');
 title('sazonalidade da serie 1')
 xlabel('t[h]')
 
 
 save seriestemp_comp.mat
 
 
 
 
 
    
    