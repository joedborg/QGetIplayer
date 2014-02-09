#include "qgetiplayer.h"
#include "ui_qgetiplayer.h"

QGetIplayer::QGetIplayer(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::QGetIplayer)
{
    ui->setupUi(this);
}

QGetIplayer::~QGetIplayer()
{
    delete ui;
}
