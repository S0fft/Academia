unit Unit3;

{$mode ObjFPC}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls, ExtCtrls, Math;

type

  { TForm3 }

  TForm3 = class(TForm)
    Button1: TButton;
    Button2: TButton;
    Button3: TButton;
    Edit1: TEdit;
    Edit2: TEdit;
    Edit3: TEdit;
    Edit4: TEdit;
    Edit5: TEdit;
    Edit6: TEdit;
    Edit7: TEdit;
    Edit8: TEdit;
    Edit9: TEdit;
    Image1: TImage;
    Label1: TLabel;
    Label10: TLabel;
    Label2: TLabel;
    Label3: TLabel;
    Label4: TLabel;
    Label5: TLabel;
    Label6: TLabel;
    Label7: TLabel;
    Label8: TLabel;
    Label9: TLabel;
    procedure Button1Click(Sender: TObject);
    procedure Button2Click(Sender: TObject);
    procedure Button3Click(Sender: TObject);
  private

  public

  end;

var
  Form3: TForm3;
  x1, y1, x2, y2, x3, y3: integer;
  x, y, z: double;
implementation

{$R *.lfm}

{ TForm3 }

procedure TForm3.Button1Click(Sender: TObject);
begin
  Image1.Canvas.Rectangle (0,0, Image1.Width, Image1.Height);
x1:= StrToInt (Edit1.Text);
y1:= StrToInt (Edit2.Text);
x2:= StrToInt (Edit3.Text);
y2:= StrToInt (Edit4.Text);
x3:= StrToInt (Edit5.Text);
y3:= StrToInt (Edit6.Text);

Image1.Canvas.Pen.Color:= clAqua;
Image1.Canvas.MoveTo (x1, y1);
Image1.Canvas.Pen.Color:= $0000FF00;
Image1.Canvas.LineTo (x2, y2);
Image1.Canvas.Pen.Color:= $00FFFF00;
Image1.Canvas.LineTo (x3, y3);
Image1.Canvas.Pen.Color:= $0000A5FF;
Image1.Canvas.LineTo (x1, y1);
end;

procedure TForm3.Button2Click(Sender: TObject);
begin
  x:=sqrt(Power(x2-x1,2)+Power(y2-y1,2));
  y:=sqrt(Power(x3-x2,2)+Power(y3-y2,2));
  z:=sqrt(Power(x1-x3,2)+Power(y1-y3,2));

  Edit7.Text:= FloattoStr(x);
  Edit8.Text:= FloattoStr(y);
  Edit9.Text:= FloattoStr(z);
end;

procedure TForm3.Button3Click(Sender: TObject);
begin
  If (x < y + z) and (y < x + z) and (z < x + y) Then Label10.Caption := 'Трикутника з цими сторонами може існувати'
Else Label10.Caption := 'Трикутника з цими сторонами НЕ може існувати';
end;

end.

