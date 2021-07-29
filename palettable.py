import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as colors
import palettable
import  numpy as np

rc={
    "font.sans-serif":"SimHei",
    "axes.unicode_minus":False,
    "xtick.direction":"in",
    "ytick.direction":"in",
    "xtick.bottom":True,
    "ytick.left":True,
    "figure.figsize":(6.4,4.8),
    'xtick.top':False,
    'ytick.right':False,
    }
plt.rcParams.update(rc)

def get_palette_data(module_name):
    cmap_dict={}
    model=getattr(palettable,module_name)
    for type in [ "diverging", "qualitative","sequential"]:
        try:
            type_colormap=getattr(model,type)
        except:
            pass
        else:
            cmap_dict[type]=getattr(type_colormap,"_NAMES_TO_DATA")
    return cmap_dict

def get_cmap(colors_data,type,name):
    colors_data=np.array(colors_data)/255
    if type == 'qualitative':
        cmap=colors.ListedColormap(colors_data,name=name)
    else:
        if len(colors_data)>30:
            cmap1=colors.ListedColormap(colors_data[0::len(colors_data)//8])
        elif len(colors_data)>8:
            cmap1=colors.ListedColormap(colors_data[0::2])
        else:
            cmap1=colors.ListedColormap(colors_data)
        cmap2=colors.LinearSegmentedColormap.from_list(name,colors_data)
        cmap=(cmap1,cmap2)
    return cmap

def get_palette_cmap(palette_data):
    cmap_dict={}
    for c_type in palette_data:
        cmap_instance_list=[]
        cmap_instance_list1=[]
        cmap_name_list=[]
        for name in palette_data[c_type]:
            cmap=get_cmap(palette_data[c_type][name],c_type,name)
            cmap_name_list.append(name)
            if c_type == 'qualitative':
                cmap_instance_list.append(cmap)
            else:
                cmap_instance_list.append(cmap[0])
                cmap_instance_list1.append(cmap[1])
        if c_type == 'qualitative':
            cmap_dict[c_type]={
                "name":cmap_name_list,
                'cmap':cmap_instance_list
            }
        else:
             cmap_dict[c_type]={
                "name":cmap_name_list,
                'cmap':(cmap_instance_list,cmap_instance_list1)
            }
    return cmap_dict

def get_palette_dict(module_name_list):
    palette_dict={}
    for module_name in module_name_list:
        palette_data=get_palette_data(module_name)
        palette_cmap=get_palette_cmap(palette_data)
        palette_dict[module_name]=palette_cmap
    return palette_dict

def get_data(color_map_type):
        filter_list=['utils','colormaps','matplotlib','print_maps','get_map','absolute_import','colordata', 'mycarta','tableau','wesanderson']
        color_map_name=list(filter(lambda x: not x.startswith("_") and x not in filter_list and not x.endswith("_r"),color_map_type))
        new=[(i.split("_")[0],i.split("_")[1]) for i in color_map_name]
        df=pd.DataFrame(new)
        df[1]=df[1].astype(int)
        color_map_name=df.groupby(0).max().reset_index().values.tolist()
        color_map_name= ['_'.join([i[0],str(i[1])]) for i in color_map_name]
        return color_map_name

def get_colormap_name(module_name):
    cmap_dict={}
    model=getattr(palettable,module_name)
    if module_name in ['matplotlib','mycarta','tableau','wesanderson']:
        type_colormap=model.__dir__()
        if module_name in ['matplotlib','mycarta','wesanderson']:
            cmap_dict['sequential']=get_data(type_colormap)
        else:
            cmap_dict['qualitative']=get_data(type_colormap)
    else:
        for cmap_type in [ "diverging","sequential",'qualitative']:
            try:
                type_colormap=getattr(model,cmap_type)
                color_map_type=type_colormap.__dir__()
            except:
                pass
            else:
                cmap_dict[cmap_type]=get_data(color_map_type)
    return cmap_dict

def get_palette_dict2(module_name_list):
    palette_dict={}
    for module_name in module_name_list:
        module=getattr(palettable,module_name)
        cmap_dict=get_colormap_name(module_name)
        data_dict={}
        for cmap_type in cmap_dict:
            name_list=[]
            cmap_list1=[]
            cmap_list2=[]
            if module_name != 'colorbrewer':
                type_module=getattr(palettable,module_name)
            else:
                type_module=getattr(module,cmap_type)
            for cmap_name in cmap_dict[cmap_type]:
                name_list.append(cmap_name.split("_")[0])
                cmap=getattr(type_module,cmap_name).mpl_colormap
                cmap_list1.append(cmap)
                cmap_list2.append(colors.ListedColormap(cmap(list(range(0,256)))[0::256//8]))
            if cmap_type != 'qualitative':
                data_dict[cmap_type]={
                    'name':name_list,
                    'cmap':(cmap_list2,cmap_list1)
                }
            else:
                data_dict[cmap_type]={
                    'name':name_list,
                    'cmap':cmap_list2
                }
        palette_dict[module_name]=data_dict
    return palette_dict
    
def plot_palette(title,name_list,cmap_list,save=True):
    gradient = np.linspace(0, 1, 256)
    gradient = np.vstack((gradient, gradient))
    figsize=(6.4,len(name_list)*0.6)
    fig,axes=plt.subplots(len(name_list),figsize=figsize)
    axes[0].set_title(title,fontsize=14,fontname='SimHei')
    for ax,name,cmap in zip(axes,name_list,cmap_list):
        ax.imshow(gradient,cmap=cmap,aspect='auto')
        ax.text(-0.01, .5, name, va='center', ha='right', fontsize=14,
                    transform=ax.transAxes,fontname='SimHei')
        ax.set_axis_off()
    plt.subplots_adjust(hspace=0.02)
    if save:
        plt.savefig(title+".svg",bbox_inches='tight',pad_inches=0)

def make_palette_show(module_name_list=[
    "cartocolors",
    "cmocean",
    "lightbartlein",
    "scientific"],save=False,flag=1):
    if flag ==1:
        palette_dict= get_palette_dict(module_name_list)
    else:
        palette_dict=get_palette_dict2(module_name_list)
    for module_name in palette_dict:
        for type in palette_dict[module_name]:
            try:
                title_name =module_name + "-" + type
                cmap_list=palette_dict[module_name][type]['cmap']
                name_list=palette_dict[module_name][type]['name']
                if type=='qualitative':
                    plot_palette(title_name,name_list,cmap_list,save=save)
                else:
                    plot_palette(title_name+"-orig",name_list,cmap_list[0],save=save)
                    plot_palette(title_name+"-interp",name_list,cmap_list[1],save=save)
            except:
                print(module_name,type)

if __name__ =="__main__":
    n1=["cartocolors","cmocean","lightbartlein","scientific"]
    n2=["colorbrewer",'matplotlib','mycarta','tableau','wesanderson']
    make_palette_show(n1,save=True,flag=1)
    make_palette_show(n2,save=True,flag=2)