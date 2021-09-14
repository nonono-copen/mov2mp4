# coding:utf-8
# 参考：https://qiita.com/dgkmtu/items/2367a73f7e2d498e6075

import  os
import  re

from    tkinter import *
from    tkinter import ttk
from    tkinter import messagebox
from    tkinter import filedialog
import  subprocess

def ffmpeg_cmd(i_filePath, o_filePath):
    # ffmpegを利用して mov ⇒ mp4に変換
    cmd = 'ffmpeg -i ' + i_filePath + ' -pix_fmt yuv420p ' + o_filePath
    # コマンド実行       
    subprocess.call(cmd, shell=True)

def convert_mov2mp4():
    inputDirPath = entry1.get()     # 入力フォルダパス
    outputDirPath = entry2.get()    # 出力フォルダパス
    conv_fileCount = 0;             # 処理ファイルカウント変数

    if not os.path.exists(inputDirPath) or not os.path.exists(outputDirPath):  # ファイルパスの入力有無を確認
        messagebox.showerror("error", "指定されたパスが存在しません。")
    else:
        # 変換対象のファイルリストを取得
        files = os.listdir(inputDirPath)                                

        # プログレスバーのサブウィンド
        progress_root = Toplevel()
        progress_root.title("実行中")

        #プログレスバーの設定
        progressbar=ttk.Progressbar(progress_root,length=300,mode="indeterminate")
        progressbar.pack()
        maximum_bar=len(files)
        value_bar=0
        progressbar.configure(maximum=maximum_bar,value=value_bar)

        for i, file in enumerate(files):
            # ファイル名と拡張子を分離
            fileName, ext = os.path.splitext(file) 
            if re.compile(ext, re.IGNORECASE).match('.mov') != None: # 拡張子がmovの時、変換コマンドを実行
                # 入力ファイルパス
                inputFilePath = os.path.join(inputDirPath, file)
                # 出力ファイルパス
                outputFile = fileName + '.mp4'
                outputFilePath = os.path.join(outputDirPath, outputFile)

                # mp4に変換
                ffmpeg_cmd(inputFilePath, outputFilePath) 

                # 変換に成功した場合、ファイル数をカウントしてプログレスバーを更新
                conv_fileCount+=1
                progressbar.configure(value=conv_fileCount)

            else:
                continue # movではない場合、飛ばして次の処理

        # 入力フォルダ内のmovをすべてmp4に完了後、メッセージボックスを表示
        progress_root.destroy()
        text = str(conv_fileCount) + ' 件のmovファイルをmp4ファイル に変換しました' 
        messagebox.showinfo("info", text)

# フォルダ指定の関数
def inputDirDialogClicked():
    iDir = os.path.dirname(os.path.abspath(__file__))       # 実行時のファイルの絶対パスを取得 
    iDirPath = filedialog.askdirectory(initialdir = iDir)   # 実行時のファイルパスから参照画面を作成
    entry1.set(iDirPath)

def outputDirDialogClicked():
    iDir = os.path.dirname(os.path.abspath(__file__))       # 実行時のファイルの絶対パスを取得 
    iDirPath = filedialog.askdirectory(initialdir = iDir)   # 実行時のファイルパスから参照画面を作成
    entry2.set(iDirPath)

# main
if __name__ == '__main__':
     # rootの作成
    root = Tk()
    root.title("動画の拡張子 変わるんです ｜ mov ⇒ mp4")

    #-------------------------------------------------------#
    # Frame1の作成
    frame1 = ttk.Frame(root, padding=10)
    frame1.grid(row=0, column=1, sticky=E)

    # 「フォルダ参照」ラベルの作成
    IDirLabel = ttk.Label(frame1, text="入力フォルダ＞＞", padding=(5, 2))
    IDirLabel.pack(side=LEFT)

    # 「フォルダ参照」エントリーの作成
    entry1 = StringVar()
    IDirEntry = ttk.Entry(frame1, textvariable=entry1, width=30)
    IDirEntry.pack(side=LEFT)

    # 「フォルダ参照」ボタンの作成
    IDirButton = ttk.Button(frame1, text="参照", command=inputDirDialogClicked)
    IDirButton.pack(side=LEFT)

    #-------------------------------------------------------#
    # Frame2の作成
    frame2 = ttk.Frame(root, padding=10)
    frame2.grid(row=2, column=1, sticky=E)

    # 「フォルダ参照」ラベルの作成
    IDirLabel2 = ttk.Label(frame2, text="出力フォルダ＞＞", padding=(5, 2))
    IDirLabel2.pack(side=LEFT)

    # 「フォルダ参照」エントリーの作成
    entry2 = StringVar()
    IDirEntry2 = ttk.Entry(frame2, textvariable=entry2, width=30)
    IDirEntry2.pack(side=LEFT)

    # 「フォルダ参照」ボタンの作成
    IDirButton2 = ttk.Button(frame2, text="参照", command=outputDirDialogClicked)
    IDirButton2.pack(side=LEFT)

    #-------------------------------------------------------#
    # Frame3の作成
    frame3 = ttk.Frame(root, padding=10)
    frame3.grid(row=5,column=1,sticky=W)

    # 実行ボタンの設置
    button1 = ttk.Button(frame3, text="実行", command=convert_mov2mp4)
    button1.pack(fill = "x", padx=30, side = "left")

    # キャンセルボタンの設置
    button2 = ttk.Button(frame3, text=("閉じる"), command=root.destroy)
    button2.pack(fill = "x", padx=30, side = "left")

    root.mainloop()

   





    