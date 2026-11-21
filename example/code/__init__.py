import mathsys as ms_module
import os as __init__module_os
import sys as __init__module_sys
__init__module_os.system('cls' if os.name == "nt" else "clear")

a = ms_module.do_so_nguyen_to_tu_a_den_z_va_dem_mknone
b = ms_module.xem_a_co_phai_la_so_nguyen_to_ko_mknone
c = ms_module.dem_xem_a_co_bao_nhieu_uoc_so_va_noi_ra_tung_uoc_so_mknone
d = ms_module.may_tinh_td_congtru_nhanchia_luythua_canbachai_canbacx_don_gian_mknone
f = ms_module.pevp_xem_mknone
def cls():
    __init__module_os.system('cls' if os.name == "nt" else "clear")
def del():
    try:
        __init__module_os.remove('a')
    finally:
        return "done"
def ver():
    return "1.0.0"
def help():
    return ms_module.helpcmd
def file():
    try:
        with open('a', 'r', encoding='utf-8') as f:
            fr = f.read()
        return fr
    except:
        pass
def quit():
    __init__module_sys.exit(0)
def exit():
    quit()
def app():
    return "cannot run due error: " + str(int("00cantruninthispy00", 36)) + "x36"