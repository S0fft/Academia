unit Unit1;

interface

uses
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants, System.Classes, Vcl.Graphics,
  Vcl.Controls, Vcl.Forms, Vcl.Dialogs, Vcl.StdCtrls;

type
  TForm1 = class(TForm)
    Edit1: TEdit;
    Button1: TButton;
    Button2: TButton;
    Label1: TLabel;
    ComboBox1: TComboBox;
    procedure Button1Click(Sender: TObject);
    procedure Button2Click(Sender: TObject);
    procedure FormActivate(Sender: TObject);
    procedure ComboBox1Change(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form1: TForm1;

implementation

{$R *.dfm}

procedure TForm1.Button1Click(Sender: TObject);
begin
  Self.Caption:= Edit1.Text;
end;

procedure TForm1.Button2Click(Sender: TObject);
begin
  Close();
end;

procedure TForm1.ComboBox1Change(Sender: TObject);
begin
  case (ComboBox1.ItemIndex) of
0: Self.BorderStyle:= bsNone;
1: Self.BorderStyle:= bsSingle;
2: Self.BorderStyle:= bsSizeable;
3: Self.BorderStyle:= bsDialog;
4: Self.BorderStyle:= bsToolWindow;
5: Self.BorderStyle:= bsSizeToolWin;
end;
end;

procedure TForm1.FormActivate(Sender: TObject);
begin
  ComboBox1.ItemIndex:= 2;
end;

end.
