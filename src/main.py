# main.py
#
# Copyright 2024 Programmer
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

try:
    from color.warna import banners
    from color.warna import orange
    from color.warna import putih
    from color.warna import merah
    from color.warna import hijau
    from color.warna import biru
    from color.warna import borange
    from color.warna import bputih
    from color.warna import bhijau
    from color.warna import bbiru
    from color.warna import bmerah
    from color.warna import kelabu
    from color.warna import borangekelip
    from color.warna import banmerah
    from color.warna import banhijau
    from color.warna import banorange
    from color.warna import reset
    import sys, os, time, webbrowser
    import subprocess
    import glob
except ImportError:
        print(' [!] Harap install ulang script ini dari repository github kami!');sys.exit()

def main():
    try:
        print(banners)
        pilih = putih+"""["""+banhijau+""">"""+reset+putih+"""] Opsi...
 """+putih+"""["""+banhijau+"""1"""+reset+putih+"""] Convert gif/video file to image(.png)
 """+putih+"""["""+banhijau+"""2"""+reset+putih+"""] Create new boot animation!
 """+putih+"""["""+banhijau+"""3"""+reset+putih+"""] Manual Change boot animation
 """+putih+"""["""+banhijau+"""4"""+reset+putih+"""] Hapus Boot Animation
 """+putih+"""["""+banhijau+"""5"""+reset+putih+"""] Preview boot animation!"""+reset
        print(pilih)
        mulai = input(kelabu+" ["+banorange+">"+reset+kelabu+"]"+orange+" Input: ")
        if mulai.lower() == "5":
            print(putih+"\n ["+banorange+"5"+reset+putih+"] Preview boot animation")
            timed = input(kelabu+" ["+orange+">"+kelabu+"]"+putih+" Jumlah waktu preview (detik): ")
            os.system('sudo plymouthd && sudo plymouth --show-splash && sleep '+timed+' && sudo plymouth --quit')
            sys.exit()

        if mulai.lower() == "4":
            print(putih+" ["+merah+"4"+putih+"]"+putih+" Penghapus boot animation!")
            print(putih+"["+banmerah+"W"+reset+putih+"] Pastikan sebelum menghapus boot animation, kamu sudah mengubah boot animation kamu ke yang lain")
            print(kelabu+"["+hijau+">"+kelabu+"]"+putih+" Daftar Boot animation yang ada")
            subprocess.run(['ls', '/usr/share/plymouth/themes'])
            s = input(putih+"["+orange+">"+putih+"]: ")
            try:
                subprocess.run(['rm', '-r', '/usr/share/plymouth/themes/'+s], check=True)
                print(kelabu+" ["+banhijau+"✔️"+reset+kelabu+"]"+putih+" Berhasil dihapus")
            except subprocess.CalledProcessError:
                print(kelabu+" ["+banmerah+"!"+reset+kelabu+"]"+putih+"Terjadi kesalahan saat menghapus atau folder memang tidak ada")
        if mulai.lower() == "1":
            print(putih+" ["+hijau+"1"+putih+"]"+putih+" Gif/Video to frame converter!")
            awal = input(kelabu+" ["+orange+">"+kelabu+"]"+putih+" Video/gif Path: ")
            akhir = input(kelabu+" ["+orange+">"+kelabu+"]"+putih+" Output Folder: ")
            file_extension = os.path.splitext(awal)[1].lower()
            if file_extension == ".gif":
                from PIL import Image
                print("")
                print(kelabu+" ["+banorange+"INFO"+reset+kelabu+"]"+orange+" Sedang diproses..."+reset)
                os.makedirs(akhir, exist_ok=True)
                with Image.open(awal) as img:
                    frames = img.n_frames
                    for i in range(frames):
                        img.seek(i)
                        outputt = os.path.join(akhir, f'animation_{i:01}.png')
                        img.save(outputt, format='PNG')
                print(putih+" ["+banhijau+"INFO"+reset+putih+"] Selesai, file disimpan di "+hijau+akhir+reset)
            if file_extension == ".mp4":
                print("")
                print(kelabu+" ["+banorange+"INFO"+reset+kelabu+"]"+orange+" Sedang diproses..."+reset)
                print(kelabu+" ["+merah+"!"+kelabu+"]"+putih+" Berjalan menggunakan subrpocess untuk ffmpeg!"+reset); time.sleep(1)
                os.makedirs(akhir, exist_ok=True)
                cmd = [ 'ffmpeg', '-i', awal, '-start_number', '0', os.path.join(akhir, 'animation_%01d.png') ]
                subprocess.run(cmd, check=True)
                print(putih+" ["+banhijau+"INFO"+reset+putih+"] Selesai, file disimpan di "+hijau+akhir+reset)

        if mulai.lower() == "2":
            print(putih+" ["+hijau+"2"+putih+"]"+putih+" Plymouth boot animation creator")
            image = input(kelabu+" ["+orange+">"+kelabu+"]"+putih+" Frame(image) Path: ")
            name = input(kelabu+" ["+orange+">"+kelabu+"]"+putih+" Nama theme untuk boot animation kamu: ")
            desc = input(kelabu+" ["+orange+">"+kelabu+"]"+putih+" Deskripsi theme boot animation kamu: ")
            speed = input(kelabu+" ["+orange+">"+kelabu+"]"+putih+" Kecepatan animasi [1(Super) 2(Sangat cepat 3(cepat) 4(normal) 5(cocok untuk seni pixel)]: ")

            os.makedirs('/usr/share/plymouth/themes/'+name, exist_ok=True)
            all_file = glob.glob(os.path.join(image, '*.png'))
            tota = len(all_file)

            plymouth = """[Plymouth Theme]
Name="""+name+"""
Description="""+desc+"""
ModuleName=script

[script]
ImageDir=/usr/share/plymouth/themes/"""+name+"""
ScriptFile=/usr/share/plymouth/themes/"""+name+"""/"""+name+""".script"""
            script = """Window.SetBackgroundTopColor (0.0, 0.00, 0.0);
Window.SetBackgroundBottomColor (0.0, 0.00, 0.0);
for (i = 0; i < """+str(tota)+"""; i++)
  flyingman_image[i] = Image("animation_" + i + ".png");
flyingman_sprite = Sprite();
flyingman_sprite.SetX(Window.GetWidth() / 2 - flyingman_image[0].GetWidth() / 2);
flyingman_sprite.SetY(Window.GetHeight() / 2 - flyingman_image[0].GetHeight() / 2);
progress = 0;

fun refresh_callback ()
  {
    flyingman_sprite.SetImage(flyingman_image[(progress / """+str(speed)+""") % """+str(tota)+"""]);
    progress++;
    Plymouth.Sleep(0.1);
  }

Plymouth.SetRefreshFunction (refresh_callback);
"""

            text_bytes = plymouth.encode('utf-8')
            with open('/usr/share/plymouth/themes/'+name+'/'+name+'.plymouth', 'wb') as file:
                file.write(text_bytes)
            text = script.encode('utf-8')
            with open('/usr/share/plymouth/themes/'+name+'/'+name+'.script', 'wb') as file:
                file.write(text)
            print(putih+" ["+banhijau+"#"+reset+putih+"] Selesai membuat file "+hijau+name+".plymouth"+putih+" dan "+hijau+name+".script"+putih)
            print(putih+" ["+banhijau+"#"+reset+putih+"] Memindahkan file gambar ke "+orange+"/usr/share/plymouth/themes/"+name+reset)
            all_files = os.listdir(image)
            image_files = [f for f in all_files if f.endswith('.png') and f.startswith('animation_')]
            for image_file in image_files:
                source_path = os.path.join(image, image_file)
                destination_path = os.path.join('/usr/share/plymouth/themes/'+name, image_file)
                subprocess.run(['sudo', 'mv', source_path, destination_path], check=True)
            print(kelabu+' ['+banhijau+'✔️'+reset+kelabu+']'+putih+' Selesai...')
            print(putih+" ["+banhijau+"#"+reset+putih+"] Menambahkan boot animation baru ke entry...")
            subprocess.run(['sudo', 'update-alternatives', '--install', '/usr/share/plymouth/themes/default.plymouth', 'default.plymouth', '/usr/share/plymouth/themes/'+name+'/'+name+'.plymouth', '100'], check=True)
            subprocess.run(['sudo', 'update-alternatives', '--config', 'default.plymouth'], check=True)
            print(kelabu+' ['+banhijau+'✔️'+reset+kelabu+']'+putih+' Selesai...')
            terapkan = input(putih+" ["+orange+"?"+reset+putih+"] Apakah anda mau menerapkan nya langsung ke initramfs? [y/n]: ")
            if terapkan.lower() == "y" or terapkan.lower() == "Y":
                print(putih+" ["+banhijau+"#"+reset+putih+"] Menerapkan konfigurasi ke initramfs...")
                subprocess.run(['sudo', 'update-initramfs', '-u'], check=True)
                print(kelabu+' ['+banhijau+'✔️'+reset+kelabu+']'+putih+' Selesai...')
                print(kelabu+' ['+hijau+'#'+reset+kelabu+']'+putih+' Terima kasih karena telah menggunakan, selamat menikmati tampilan boot animation anda'); sys.exit()
            else:
                print(kelabu+' ['+hijau+'#'+reset+kelabu+']'+putih+' Terima kasih karena telah menggunakan, selamat menikmati tampilan boot animation anda'); sys.exit()
                print(kelabu+' ['+banhijau+'#'+reset+kelabu+']'+putih+' Silahkan ketik sendiri "sudo update-initramfs -u" tapi tetap berhati hati dengan command tersebut'+reset);sys.exit()
        if mulai.lower() == "3":
            print(putih+" ["+hijau+"3"+putih+"]"+putih+" Plymouth boot anmiation changer!")
            print(kelabu+' ['+orange+'#'+reset+kelabu+']'+putih+' Memulai subprocess...')
            print(kelabu+" ["+orange+"#"+reset+kelabu+"]"+putih+" Menjalankan update-alternatives...")
            subprocess.run(['sudo', 'update-alternatives', '--config', 'default.plymouth'], check=True)
            print(kelabu+' ['+orange+'~'+reset+kelabu+']'+putih+' Memperbarui Initramfs...')
            subprocess.run(['sudo', 'update-initramfs', '-u'], check=True)
            print(kelabu+' ['+banhijau+'✔️'+reset+kelabu+']'+putih+' Selesai...')
        
    except (KeyboardInterrupt, EOFError): print(putih+" ["+banmerah+"!"+reset+putih+"] Exit..."+reset); sys.exit()
if __name__=="__main__":
    main()
