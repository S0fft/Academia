unit Unit2;

{$mode ObjFPC}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls;

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
    procedure Button1Click(Sender: TObject);
    procedure Edit4Change(Sender: TObject);
    procedure FormCreate(Sender: TObject);
  private

  public

  end;

var
  Form2: TForm2;

implementation

{$R *.lfm}

{ TForm2 }

procedure TForm2.FormCreate(Sender: TObject);
begin

end;

procedure TForm2.Edit4Change(Sender: TObject);
begin

end;

procedure TForm2.Button1Click(Sender: TObject);
begin
  procedure TForm2.Button1Click(Sender: TObject);
var
  x, y, z, result: Double;
begin
  // Чтение данных из полей ввода
  x := StrToFloat(Edit1.Text);
  y := StrToFloat(Edit2.Text);
  z := StrToFloat(Edit3.Text);

  // Вычисление функции
  result := Power(2, -x) * Power(x + Power(Abs(y), 1 / 4), 1 / 3) * Power((Exp(x) - 1) / Sin(z), 1 / 3);

  // Вывод результата
  Edit4.Text := FloatToStr(result);
end;

end;

end.

