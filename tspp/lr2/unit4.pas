unit Unit4;

{$mode ObjFPC}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls, ExtCtrls;

type

  { TForm4 }

  TForm4 = class(TForm)
    Button1: TButton;
    Edit1: TEdit;
    Edit2: TEdit;
    Edit3: TEdit;
    Image1: TImage;
    Label1: TLabel;
    Label2: TLabel;
    Label3: TLabel;
    procedure Button1Click(Sender: TObject);
  private

  public

  end;

const
g = 10;

var
  Form4: TForm4;
  v, t, tmax, x, y, a, xmax, ymax, kx, ky, dt: real;
  N, xsc, ysc: integer;

implementation

{$R *.lfm}

{ TForm4 }

procedure TForm4.Button1Click(Sender: TObject);
begin
Image1.Canvas.Pen.Color:= clWhite;
Image1.Canvas.Rectangle (0, 0, Image1.Width, Image1.Height);
Image1.Canvas.pen.Color:= clBlack;

n:= strtoint (Edit1.Text);
v:= strtofloat (Edit2.Text);
a:= strtofloat (Edit3.Text);
A:= A * Pi / 180;
t:= 0;
tmax:= 2 * V * sin (a) / g;
dt:= tmax / N;
xmax:= V * V / g;
ymax:= (V * V / g) / 2;
kx:= Image1.Width / xmax;
ky:= Image1.Height / ymax;
while t <= tmax do
begin
y:= V * sin (a) * t - g * t * t / 2;
x:= V * cos (A) * t;
ysc:= round (Image1.Height - y * ky);
xsc:= round (x * kx);
Image1.Canvas.Ellipse (xsc-1, ysc-1, xsc + 1, ysc + 1);
t:= t + dt;
end;
end;

end.

