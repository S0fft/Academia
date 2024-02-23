object Form1: TForm1
  Left = 0
  Top = 0
  AlphaBlend = True
  Caption = 'Evgeniy_Pelikh_IST-21-1'
  ClientHeight = 266
  ClientWidth = 551
  Color = clBackground
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'Tahoma'
  Font.Style = []
  TextHeight = 13
  object Button1: TButton
    Left = 8
    Top = 201
    Width = 75
    Height = 33
    Caption = 'Close'
    TabOrder = 0
    OnClick = Button1Click
  end
  object BHeight: TButton
    Left = 168
    Top = 24
    Width = 91
    Height = 32
    Caption = '+ '#1042#1080#1089#1086#1090#1072
    Default = True
    TabOrder = 1
    OnClick = BHeightClick
  end
  object BWidth: TButton
    Left = 288
    Top = 24
    Width = 89
    Height = 32
    Cancel = True
    Caption = '+ '#1064#1080#1088#1080#1085#1072
    TabOrder = 2
    OnClick = BWidthClick
  end
  object BSize: TButton
    Left = 8
    Top = 152
    Width = 73
    Height = 33
    Caption = 'Default'
    TabOrder = 3
    OnClick = BSizeClick
  end
  object BXPlus: TButton
    Left = 288
    Top = 72
    Width = 89
    Height = 33
    Caption = #1055#1088#1072#1074#1086#1088#1091#1095' (+X)'
    TabOrder = 4
    OnClick = BXPlusClick
  end
  object BYPlus: TButton
    Left = 288
    Top = 128
    Width = 89
    Height = 33
    Caption = #1042#1085#1080#1079' (+Y)'
    TabOrder = 5
    OnClick = BYPlusClick
  end
  object BXMinus: TButton
    Left = 168
    Top = 72
    Width = 91
    Height = 33
    Caption = #1051#1110#1074#1086#1088#1091#1095' (-X)'
    TabOrder = 6
    OnClick = BXMinusClick
  end
  object BYMinus: TButton
    Left = 168
    Top = 128
    Width = 91
    Height = 33
    Caption = #1042#1075#1086#1088#1091' (-Y)'
    TabOrder = 7
    OnClick = BYMinusClick
  end
  object OpacityPlus: TButton
    Left = 288
    Top = 180
    Width = 89
    Height = 37
    Caption = '+ '#1055#1088#1086#1079#1086#1088#1110#1089#1090#1100
    TabOrder = 8
    OnClick = OpacityPlusClick
  end
  object OpacityMinus: TButton
    Left = 168
    Top = 180
    Width = 91
    Height = 37
    Caption = '- '#1055#1088#1086#1079#1086#1088#1110#1089#1090#1100
    TabOrder = 9
    OnClick = OpacityMinusClick
  end
end
