import numpy as np
import matAPILib

matApi = matAPILib.MatApi()

# readfile
mat = matApi.readMatFile("V.mat")


select = 4
display = 1

V = matApi.array_diff(mat["V"], matApi.min(mat["V"]))


n = matApi.vectorLength(V)

print("N -> " + str(n))

#definition of local variables
buffer = matApi.zeros(n,1)
criterion = matApi.zeros(n,1)
if select < 1:
    minDist = n/20
else:
    minDist = n/select

#horizons = np.round(np.linspace(1,np.ceil(n/20),50));
horizons = matApi.unique(np.round(matApi.logspace(0,2,50)/100*np.ceil(n/20)))
#horizons=1:2:50;
Vorig = V
#all this tempMat stuff is to avoid calling findpeaks which is horribly
# slow for our purpose
tempMat = matApi.zeros(n,3)
tempMat[0][0]=float("inf")
tempMat[-1][2]=float("inf")

# loop over scales
for is_m in range(0, matApi.vectorLength(horizons)):
    
    # sooth data, using fft-based convolution with a half sinusoid
    horizon = horizons[is_m]
    print(horizon)
    if horizon > 1:
        w=np.max(np.eps,np.sin(2*np.pi*(range(0,horizon)))/2/(horizon-1))

        w=w/matApi.sum(w);   
        print(w) 
        #V=.np.convolve(V,w,mode='same');
        V = np.real(np.fft.ifft(V,n+horizon)*np.fft(w,n+horizon))
        V = V[1+np.floor(horizon/2):np.ceil(horizon/2)]
     
    #   find local maxima
    end = -1
    tempMat[2:end] = V[1:end-1]
    # tempMat[:,2] = V
    # tempMat[1:end-1,3] = V[2:end]
#     [useless,posMax] =max(tempMat,[],2)
#     I = matApi.find(posMax)
#     I = np.gradient(I)
#     II = np.gradient(I)
    
#     #initialize buffer
#     newbuffer = matApi.zeros(n, 1)
    
#     if is_m == 1:
#         # if first iteration, keep all local maxima
#         newbuffer = Vorig(I)
#     else:    
#         old = matApi.find(newbuffer)
#         print(old)
#         old = np.gradient(old)
#         if matApi.isempty(old):
#             continue
        
# #         %Now, for each element of I, find the closest element in
# #         %old along with its distance. The few nice lines below were
# #         %written by Roger Stafford in a forum post available here:
# #         %http://www.mathworks.fr/matlabcentral/newsreader/view_thread/24387
#         [c,p] = np.sort(old)
#         #C = np.gradient(c);
#         [useless,ic] = np.histc(I,[-float("inf"),(c[1:-2]+c[2:-1])/2,float("inf")])
#         iOld = p(ic)
#         d = abs(I-old(iOld));
#         %D = d';
 
#         %done, now select only those that are sufficiently close
#         neighbours = iOld(d<minDist);
#         if ~isempty(neighbours)
#             B=V(old(neighbours))*is^2;
#             newBuffer(old(neighbours)) = B;
#         end
#     end
#     %update stuff
#     buffer = newBuffer;
#     criterion = criterion + newBuffer;
# end
# %normalize criterion
# criterion = criterion/max(criterion);
# %find peaks based on criterion
# if select<1
#     peaks = find(criterion>select);
# else
# %     sorted = find(criterion>1E-3);
# %     [~,order] = sort(criterion(sorted),'descend');
# %     peaks = sorted(order(1:min(length(sorted),select)));
#     [a,order] = sort(criterion,'descend');
#     peaks = order(1:select);
# end
# if display
#     %display
#     clf
#     plot(Vorig,'LineWidth',2);
#     hold on
#     plot(criterion*max(Vorig),'r');
#     hold on
#     plot(peaks,Vorig(peaks),'ro','MarkerSize',10,'LineWidth',2)
#     grid on
#     title('Scale-space peak detection','FontSize',16);
#     legend('data','computed criterion','selected peaks');
# end

