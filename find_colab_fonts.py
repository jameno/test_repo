{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "find_colab_fonts.ipynb",
      "version": "0.3.2",
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/jameno/test_repo/blob/test_branch/find_colab_fonts.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "8s5U0ifEhECr",
        "colab_type": "code",
        "outputId": "71998a81-d44a-4e06-8497-e68ffc870050",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "# This is a commented description\n",
        "import os\n",
        "os.getcwd()"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'/content'"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 1
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "9loAQt7bhMqF",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "import pandas as pd\n",
        "test_df = pd.DataFrame([])\n",
        "test_df.to_csv('test.csv')"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "i1HVlt35hWtv",
        "colab_type": "code",
        "outputId": "8376b08a-44a5-4c2e-cc22-dc0cf19093f4",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        }
      },
      "source": [
        "import subprocess\n",
        "p = subprocess.Popen([\"find\", \"..\", \"-type\", \"f\", \"-name\", \"*.ttf\"], stdout=subprocess.PIPE)\n",
        "print(type(p))\n",
        "#p = subprocess.Popen([\"find . -type f -name \\\"*.txt\\\"\"], stdout=subprocess.PIPE)\n",
        "\n",
        "pd.Series(p.communicate())[0].decode(\"utf-8\").split('\\n')"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "<class 'subprocess.Popen'>\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['../usr/share/fonts/truetype/liberation/LiberationSans-BoldItalic.ttf',\n",
              " '../usr/share/fonts/truetype/liberation/LiberationSansNarrow-Bold.ttf',\n",
              " '../usr/share/fonts/truetype/liberation/LiberationSansNarrow-BoldItalic.ttf',\n",
              " '../usr/share/fonts/truetype/liberation/LiberationSansNarrow-Regular.ttf',\n",
              " '../usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf',\n",
              " '../usr/share/fonts/truetype/liberation/LiberationSansNarrow-Italic.ttf',\n",
              " '../usr/share/fonts/truetype/liberation/LiberationMono-Bold.ttf',\n",
              " '../usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf',\n",
              " '../usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf',\n",
              " '../usr/share/fonts/truetype/liberation/LiberationMono-BoldItalic.ttf',\n",
              " '../usr/share/fonts/truetype/liberation/LiberationMono-Italic.ttf',\n",
              " '../usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf',\n",
              " '../usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf',\n",
              " '../usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf',\n",
              " '../usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf',\n",
              " '../usr/share/fonts/truetype/liberation/LiberationSerif-BoldItalic.ttf',\n",
              " '../usr/share/qt5/doc/global/template/style/icomoon.ttf',\n",
              " '../usr/share/tesseract-ocr/4.00/tessdata/pdf.ttf',\n",
              " '../usr/lib/R/site-library/rmarkdown/rmd/ioslides/ioslides-13.5.1/fonts/OpenSansSemiboldItalic.ttf',\n",
              " '../usr/lib/R/site-library/rmarkdown/rmd/ioslides/ioslides-13.5.1/fonts/SourceCodePro.ttf',\n",
              " '../usr/lib/R/site-library/rmarkdown/rmd/ioslides/ioslides-13.5.1/fonts/OpenSans.ttf',\n",
              " '../usr/lib/R/site-library/rmarkdown/rmd/ioslides/ioslides-13.5.1/fonts/OpenSansSemibold.ttf',\n",
              " '../usr/lib/R/site-library/rmarkdown/rmd/ioslides/ioslides-13.5.1/fonts/OpenSansItalic.ttf',\n",
              " '../usr/lib/R/site-library/rmarkdown/rmd/h/fontawesome/webfonts/fa-regular-400.ttf',\n",
              " '../usr/lib/R/site-library/rmarkdown/rmd/h/fontawesome/webfonts/fa-brands-400.ttf',\n",
              " '../usr/lib/R/site-library/rmarkdown/rmd/h/fontawesome/webfonts/fa-solid-900.ttf',\n",
              " '../usr/lib/R/site-library/rmarkdown/rmd/h/ionicons/fonts/ionicons.ttf',\n",
              " '../usr/lib/R/site-library/rmarkdown/rmd/h/bootstrap/fonts/glyphicons-halflings-regular.ttf',\n",
              " '../usr/lib/R/site-library/rmarkdown/rmd/h/bootstrap/css/fonts/Ubuntu.ttf',\n",
              " '../usr/lib/R/site-library/rmarkdown/rmd/h/bootstrap/css/fonts/NewsCycleBold.ttf',\n",
              " '../usr/lib/R/site-library/rmarkdown/rmd/h/bootstrap/css/fonts/LatoBold.ttf',\n",
              " '../usr/lib/R/site-library/rmarkdown/rmd/h/bootstrap/css/fonts/Raleway.ttf',\n",
              " '../usr/lib/R/site-library/rmarkdown/rmd/h/bootstrap/css/fonts/Lato.ttf',\n",
              " '../usr/lib/R/site-library/rmarkdown/rmd/h/bootstrap/css/fonts/OpenSansBoldItalic.ttf',\n",
              " '../usr/lib/R/site-library/rmarkdown/rmd/h/bootstrap/css/fonts/RobotoBold.ttf',\n",
              " '../usr/lib/R/site-library/rmarkdown/rmd/h/bootstrap/css/fonts/OpenSansBold.ttf',\n",
              " '../usr/lib/R/site-library/rmarkdown/rmd/h/bootstrap/css/fonts/SourceSansProItalic.ttf',\n",
              " '../usr/lib/R/site-library/rmarkdown/rmd/h/bootstrap/css/fonts/SourceSansProLight.ttf',\n",
              " '../usr/lib/R/site-library/rmarkdown/rmd/h/bootstrap/css/fonts/Roboto.ttf',\n",
              " '../usr/lib/R/site-library/rmarkdown/rmd/h/bootstrap/css/fonts/RobotoMedium.ttf',\n",
              " '../usr/lib/R/site-library/rmarkdown/rmd/h/bootstrap/css/fonts/SourceSansProBold.ttf',\n",
              " '../usr/lib/R/site-library/rmarkdown/rmd/h/bootstrap/css/fonts/LatoItalic.ttf',\n",
              " '../usr/lib/R/site-library/rmarkdown/rmd/h/bootstrap/css/fonts/RalewayBold.ttf',\n",
              " '../usr/lib/R/site-library/rmarkdown/rmd/h/bootstrap/css/fonts/OpenSans.ttf',\n",
              " '../usr/lib/R/site-library/rmarkdown/rmd/h/bootstrap/css/fonts/SourceSansPro.ttf',\n",
              " '../usr/lib/R/site-library/rmarkdown/rmd/h/bootstrap/css/fonts/OpenSansItalic.ttf',\n",
              " '../usr/lib/R/site-library/rmarkdown/rmd/h/bootstrap/css/fonts/NewsCycle.ttf',\n",
              " '../usr/lib/R/site-library/rmarkdown/rmd/h/bootstrap/css/fonts/RobotoLight.ttf',\n",
              " '../usr/lib/R/site-library/rmarkdown/rmd/h/bootstrap/css/fonts/OpenSansLightItalic.ttf',\n",
              " '../usr/lib/R/site-library/rmarkdown/rmd/h/bootstrap/css/fonts/OpenSansLight.ttf',\n",
              " '../usr/local/lib/python3.6/dist-packages/notebook/static/components/font-awesome/fonts/fontawesome-webfont.ttf',\n",
              " '../usr/local/lib/python3.6/dist-packages/werkzeug/debug/shared/ubuntu.ttf',\n",
              " '../usr/local/lib/python3.6/dist-packages/matplotlib/tests/mpltest.ttf',\n",
              " '../usr/local/lib/python3.6/dist-packages/matplotlib/mpl-data/fonts/ttf/cmss10.ttf',\n",
              " '../usr/local/lib/python3.6/dist-packages/matplotlib/mpl-data/fonts/ttf/STIXSizFourSymReg.ttf',\n",
              " '../usr/local/lib/python3.6/dist-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSerif.ttf',\n",
              " '../usr/local/lib/python3.6/dist-packages/matplotlib/mpl-data/fonts/ttf/STIXSizTwoSymBol.ttf',\n",
              " '../usr/local/lib/python3.6/dist-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSans-BoldOblique.ttf',\n",
              " '../usr/local/lib/python3.6/dist-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSerif-BoldItalic.ttf',\n",
              " '../usr/local/lib/python3.6/dist-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSansMono.ttf',\n",
              " '../usr/local/lib/python3.6/dist-packages/matplotlib/mpl-data/fonts/ttf/STIXNonUniBolIta.ttf',\n",
              " '../usr/local/lib/python3.6/dist-packages/matplotlib/mpl-data/fonts/ttf/cmmi10.ttf',\n",
              " '../usr/local/lib/python3.6/dist-packages/matplotlib/mpl-data/fonts/ttf/STIXNonUniIta.ttf',\n",
              " '../usr/local/lib/python3.6/dist-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSerif-Italic.ttf',\n",
              " '../usr/local/lib/python3.6/dist-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSans.ttf',\n",
              " '../usr/local/lib/python3.6/dist-packages/matplotlib/mpl-data/fonts/ttf/STIXSizOneSymBol.ttf',\n",
              " '../usr/local/lib/python3.6/dist-packages/matplotlib/mpl-data/fonts/ttf/STIXGeneralItalic.ttf',\n",
              " '../usr/local/lib/python3.6/dist-packages/matplotlib/mpl-data/fonts/ttf/STIXSizOneSymReg.ttf',\n",
              " '../usr/local/lib/python3.6/dist-packages/matplotlib/mpl-data/fonts/ttf/cmsy10.ttf',\n",
              " '../usr/local/lib/python3.6/dist-packages/matplotlib/mpl-data/fonts/ttf/STIXNonUni.ttf',\n",
              " '../usr/local/lib/python3.6/dist-packages/matplotlib/mpl-data/fonts/ttf/STIXSizFourSymBol.ttf',\n",
              " '../usr/local/lib/python3.6/dist-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSerifDisplay.ttf',\n",
              " '../usr/local/lib/python3.6/dist-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSansMono-Oblique.ttf',\n",
              " '../usr/local/lib/python3.6/dist-packages/matplotlib/mpl-data/fonts/ttf/STIXGeneralBol.ttf',\n",
              " '../usr/local/lib/python3.6/dist-packages/matplotlib/mpl-data/fonts/ttf/STIXSizTwoSymReg.ttf',\n",
              " '../usr/local/lib/python3.6/dist-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSansDisplay.ttf',\n",
              " '../usr/local/lib/python3.6/dist-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSerif-Bold.ttf',\n",
              " '../usr/local/lib/python3.6/dist-packages/matplotlib/mpl-data/fonts/ttf/cmtt10.ttf',\n",
              " '../usr/local/lib/python3.6/dist-packages/matplotlib/mpl-data/fonts/ttf/cmr10.ttf',\n",
              " '../usr/local/lib/python3.6/dist-packages/matplotlib/mpl-data/fonts/ttf/STIXGeneral.ttf',\n",
              " '../usr/local/lib/python3.6/dist-packages/matplotlib/mpl-data/fonts/ttf/STIXNonUniBol.ttf',\n",
              " '../usr/local/lib/python3.6/dist-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSans-Oblique.ttf',\n",
              " '../usr/local/lib/python3.6/dist-packages/matplotlib/mpl-data/fonts/ttf/STIXSizFiveSymReg.ttf',\n",
              " '../usr/local/lib/python3.6/dist-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSansMono-Bold.ttf',\n",
              " '../usr/local/lib/python3.6/dist-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSansMono-BoldOblique.ttf',\n",
              " '../usr/local/lib/python3.6/dist-packages/matplotlib/mpl-data/fonts/ttf/STIXSizThreeSymBol.ttf',\n",
              " '../usr/local/lib/python3.6/dist-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSans-Bold.ttf',\n",
              " '../usr/local/lib/python3.6/dist-packages/matplotlib/mpl-data/fonts/ttf/STIXSizThreeSymReg.ttf',\n",
              " '../usr/local/lib/python3.6/dist-packages/matplotlib/mpl-data/fonts/ttf/cmb10.ttf',\n",
              " '../usr/local/lib/python3.6/dist-packages/matplotlib/mpl-data/fonts/ttf/STIXGeneralBolIta.ttf',\n",
              " '../usr/local/lib/python3.6/dist-packages/matplotlib/mpl-data/fonts/ttf/cmex10.ttf',\n",
              " '../usr/local/lib/python3.6/dist-packages/wordcloud/DroidSansMono.ttf',\n",
              " '../usr/local/lib/python3.6/dist-packages/imgaug/DejaVuSans.ttf',\n",
              " '../usr/local/lib/python2.7/dist-packages/notebook/static/components/font-awesome/fonts/fontawesome-webfont.ttf',\n",
              " '../usr/local/lib/python2.7/dist-packages/werkzeug/debug/shared/ubuntu.ttf',\n",
              " '../usr/local/lib/python2.7/dist-packages/matplotlib/tests/mpltest.ttf',\n",
              " '../usr/local/lib/python2.7/dist-packages/matplotlib/mpl-data/fonts/ttf/cmss10.ttf',\n",
              " '../usr/local/lib/python2.7/dist-packages/matplotlib/mpl-data/fonts/ttf/STIXSizFourSymReg.ttf',\n",
              " '../usr/local/lib/python2.7/dist-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSerif.ttf',\n",
              " '../usr/local/lib/python2.7/dist-packages/matplotlib/mpl-data/fonts/ttf/STIXSizTwoSymBol.ttf',\n",
              " '../usr/local/lib/python2.7/dist-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSans-BoldOblique.ttf',\n",
              " '../usr/local/lib/python2.7/dist-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSerif-BoldItalic.ttf',\n",
              " '../usr/local/lib/python2.7/dist-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSansMono.ttf',\n",
              " '../usr/local/lib/python2.7/dist-packages/matplotlib/mpl-data/fonts/ttf/STIXNonUniBolIta.ttf',\n",
              " '../usr/local/lib/python2.7/dist-packages/matplotlib/mpl-data/fonts/ttf/cmmi10.ttf',\n",
              " '../usr/local/lib/python2.7/dist-packages/matplotlib/mpl-data/fonts/ttf/STIXNonUniIta.ttf',\n",
              " '../usr/local/lib/python2.7/dist-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSerif-Italic.ttf',\n",
              " '../usr/local/lib/python2.7/dist-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSans.ttf',\n",
              " '../usr/local/lib/python2.7/dist-packages/matplotlib/mpl-data/fonts/ttf/STIXSizOneSymBol.ttf',\n",
              " '../usr/local/lib/python2.7/dist-packages/matplotlib/mpl-data/fonts/ttf/STIXGeneralItalic.ttf',\n",
              " '../usr/local/lib/python2.7/dist-packages/matplotlib/mpl-data/fonts/ttf/STIXSizOneSymReg.ttf',\n",
              " '../usr/local/lib/python2.7/dist-packages/matplotlib/mpl-data/fonts/ttf/cmsy10.ttf',\n",
              " '../usr/local/lib/python2.7/dist-packages/matplotlib/mpl-data/fonts/ttf/STIXNonUni.ttf',\n",
              " '../usr/local/lib/python2.7/dist-packages/matplotlib/mpl-data/fonts/ttf/STIXSizFourSymBol.ttf',\n",
              " '../usr/local/lib/python2.7/dist-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSerifDisplay.ttf',\n",
              " '../usr/local/lib/python2.7/dist-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSansMono-Oblique.ttf',\n",
              " '../usr/local/lib/python2.7/dist-packages/matplotlib/mpl-data/fonts/ttf/STIXGeneralBol.ttf',\n",
              " '../usr/local/lib/python2.7/dist-packages/matplotlib/mpl-data/fonts/ttf/STIXSizTwoSymReg.ttf',\n",
              " '../usr/local/lib/python2.7/dist-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSansDisplay.ttf',\n",
              " '../usr/local/lib/python2.7/dist-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSerif-Bold.ttf',\n",
              " '../usr/local/lib/python2.7/dist-packages/matplotlib/mpl-data/fonts/ttf/cmtt10.ttf',\n",
              " '../usr/local/lib/python2.7/dist-packages/matplotlib/mpl-data/fonts/ttf/cmr10.ttf',\n",
              " '../usr/local/lib/python2.7/dist-packages/matplotlib/mpl-data/fonts/ttf/STIXGeneral.ttf',\n",
              " '../usr/local/lib/python2.7/dist-packages/matplotlib/mpl-data/fonts/ttf/STIXNonUniBol.ttf',\n",
              " '../usr/local/lib/python2.7/dist-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSans-Oblique.ttf',\n",
              " '../usr/local/lib/python2.7/dist-packages/matplotlib/mpl-data/fonts/ttf/STIXSizFiveSymReg.ttf',\n",
              " '../usr/local/lib/python2.7/dist-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSansMono-Bold.ttf',\n",
              " '../usr/local/lib/python2.7/dist-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSansMono-BoldOblique.ttf',\n",
              " '../usr/local/lib/python2.7/dist-packages/matplotlib/mpl-data/fonts/ttf/STIXSizThreeSymBol.ttf',\n",
              " '../usr/local/lib/python2.7/dist-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSans-Bold.ttf',\n",
              " '../usr/local/lib/python2.7/dist-packages/matplotlib/mpl-data/fonts/ttf/STIXSizThreeSymReg.ttf',\n",
              " '../usr/local/lib/python2.7/dist-packages/matplotlib/mpl-data/fonts/ttf/cmb10.ttf',\n",
              " '../usr/local/lib/python2.7/dist-packages/matplotlib/mpl-data/fonts/ttf/STIXGeneralBolIta.ttf',\n",
              " '../usr/local/lib/python2.7/dist-packages/matplotlib/mpl-data/fonts/ttf/cmex10.ttf',\n",
              " '../usr/local/lib/python2.7/dist-packages/wordcloud/DroidSansMono.ttf',\n",
              " '../usr/local/lib/python2.7/dist-packages/imgaug/DejaVuSans.ttf',\n",
              " '../tensorflow-2.0.0b1/python3.6/werkzeug/debug/shared/ubuntu.ttf',\n",
              " '../tensorflow-2.0.0b1/python2.7/werkzeug/debug/shared/ubuntu.ttf',\n",
              " '']"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 26
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ImTWG9PAigPr",
        "colab_type": "code",
        "outputId": "7d0b6fc4-c760-4cdd-d493-12d10d7b99f7",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 283
        }
      },
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "error",
          "ename": "ValueError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mValueError\u001b[0m                                Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-10-389dd681107b>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcommunicate\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;32m/usr/lib/python3.6/subprocess.py\u001b[0m in \u001b[0;36mcommunicate\u001b[0;34m(self, input, timeout)\u001b[0m\n\u001b[1;32m    848\u001b[0m                 \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_stdin_write\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0minput\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    849\u001b[0m             \u001b[0;32melif\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstdout\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 850\u001b[0;31m                 \u001b[0mstdout\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstdout\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mread\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    851\u001b[0m                 \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstdout\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mclose\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    852\u001b[0m             \u001b[0;32melif\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstderr\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mValueError\u001b[0m: read of closed file"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "pglUZ-vNi6JF",
        "colab_type": "code",
        "outputId": "70c82b67-2630-42d4-8ef8-7402622e6ad6",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 68
        }
      },
      "source": [
        "test_str = \"../usr/share/fonts/truetype/liberation/LiberationSans-BoldItalic.ttf\\\\n../usr/share/fonts/truetype/liberation/LiberationSansNarrow-Bold.ttf\\\\n\"\n",
        "test_str.split('\\\\n')"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['../usr/share/fonts/truetype/liberation/LiberationSans-BoldItalic.ttf',\n",
              " '../usr/share/fonts/truetype/liberation/LiberationSansNarrow-Bold.ttf',\n",
              " '']"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 13
        }
      ]
    }
  ]
}