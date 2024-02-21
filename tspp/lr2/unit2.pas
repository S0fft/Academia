unit Unit2;

{$mode ObjFPC}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls, Math;

type

  { TForm2 }

  TForm2 = class(TForm)
    Button1: TButton;
    Edit1: TEdit;
    Edit2: TEdit;
    Edit3: TEdit;
    Edit4: TEdit;
    Label1: TLabel;
    Label2: TLabel;
    Label3: TLabel;
    Label4: TLabel;
    procedure Button1Click(Sender: TObject);
  private

  public

  end;

var
  Form2: TForm2;

implementation

{$R *.lfm}

{ TForm2 }

procedure TForm2.Button1Click(Sender: TObject);
var x,y,z:float;
  b: double;
begin
x:= StrtoFloat(Edit1.Text);
y:= StrtoFloat(Edit2.Text);
z:= StrtoFloat(Edit3.Text);

b:= Power(y, Power(Abs(x), 1/3)) + (Power(Cos(y), 3) * (Abs(x - y) * (1 + Power(Sin(z), 2) / Sqrt(x + y)))) / Exp(Abs(x - y)) + x / 2;

Edit4.Text:= FloattoStr(b);
end;


end.

