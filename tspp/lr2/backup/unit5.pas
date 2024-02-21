unit Unit5;

{$mode ObjFPC}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls, ExtCtrls,
  TAGraph, TASeries, Math;

type

  { TForm5 }

  TForm5 = class(TForm)
    Button1: TButton;
    Chart1: TChart;
    Chart1LineSeries1: TLineSeries;
    Edit1: TEdit;
    Edit2: TEdit;
    Edit3: TEdit;
    Label1: TLabel;
    Label2: TLabel;
    Label3: TLabel;
    procedure Button1Click(Sender: TObject);
  private

  public

  end;

var
  Form5: TForm5;
  x, y, z : real;
  i,n: integer;

implementation

{$R *.lfm}

{ TForm5 }

function fx(x: real): real;
begin
    fx:= Power(2,-x)*sqrt(x+Power(sqrt(abs(y)),1/4))*Power(sqrt(exp((x-1)/sin(z))),1/3);
end;

procedure TForm5.Button1Click(Sender: TObject);
begin
y:= strtofloat (Edit1.Text);
z:= strtofloat (Edit2.Text);
n:= strtoint (Edit3.Text);
x:= 0;
Chart1LineSeries1.Clear;
for i:= 0 to N-1 do
  begin
    x:= i /(N - 1);
    Chart1LineSeries1.AddXY(x, fx(x));
  end;
end;

end.

